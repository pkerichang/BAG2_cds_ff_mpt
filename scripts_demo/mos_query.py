# -*- coding: utf-8 -*-

import pprint

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

import bag
import bag.tech.mos


def plot_data(name='gm', mos_type='nch', vgs_min=None, vds_min=None):
    """Get interpolation function and plot/query."""
    env_list = ['tt', 'ff', 'ss', 'fs', 'sf', 'ff_hot', 'ss_hot']
    l = 60e-9
    intent = 'lvt'
    w = 0.5e-6
    vbs = 0.0
    nvds = 41
    nvgs = 81

    mos_config = bag.BagProject().tech_info.tech_params['mos']
    root_dir = mos_config['mos_char_root']

    db = bag.tech.mos.MosCharDB(root_dir, mos_type, ['intent', 'l'],
                                env_list, intent=intent, l=l,
                                method='spline')

    f = db.get_function(name)
    params, prange = db.get_fun_sweep_params()

    vds_min2, vds_max = prange[params.index('vds')]
    vgs_min2, vgs_max = prange[params.index('vgs')]

    if vgs_min is None:
        vgs_min = vgs_min2
    if vds_min is None:
        vds_min = vds_min2
    vgs_min = max(vgs_min, vgs_min2)
    vds_min = max(vds_min, vds_min2)

    # query values.
    pprint.pprint(db.query(w=w, vbs=vbs,
                           vgs=(vgs_min + vgs_max) / 2.0,
                           vds=(vds_min + vds_max) / 2.0))

    vds_vec = np.linspace(vds_min, vds_max, nvds, endpoint=True)
    vgs_vec = np.linspace(vgs_min, vgs_max, nvgs, endpoint=True)

    w, vbs, vds, vgs = np.meshgrid([w], [vbs], vds_vec, vgs_vec, indexing='ij')

    arg = np.stack([w, vbs, vds, vgs], axis=4)
    ans = f(arg)

    vds = vds.reshape([nvds, nvgs])
    vgs = vgs.reshape([nvds, nvgs])
    ans = ans.reshape([nvds, nvgs, len(env_list)])

    for idx, env in enumerate(env_list):
        fig = plt.figure(idx + 1)
        ax = fig.add_subplot(111, projection='3d')
        print('%s: %s = %.4g' % (env, name, ans[-1, -1, idx]))
        ax.plot_surface(vds, vgs, ans[..., idx], rstride=1, cstride=1, linewidth=0, cmap=cm.cubehelix)
        ax.set_title('%s__%s' % (name, env))
        ax.set_xlabel('Vds')
        ax.set_ylabel('Vgs')

    plt.show()


def optimize(adj_bias=True, opt_package='pyoptsparse', opt_method='IPOPT'):
    """Find w and vgs that optimizes the gain."""
    env_list = ['tt', 'ff']
    l = 60e-9
    intent = 'lvt'
    debug = False

    mos_config = bag.BagProject().tech_info.tech_params['mos']
    root_dir = mos_config['mos_char_root']

    db = bag.tech.mos.MosCharDB(root_dir, 'nch', ['intent', 'l'],
                                env_list, intent=intent, l=l,
                                method='spline',
                                opt_package=opt_package,
                                opt_method=opt_method,
                                # opt_settings=dict(
                                #     
                                #     ),
                                )

    ndim = len(env_list)
    vds_dim = ndim if adj_bias else 1
    objective = 'obj'
    define = [
        # set vds = vgs (vin = vout)
        ('vds = vgs', vds_dim),
        # compute gain
        # ('gain = gm / gds', ndim),
        # compute bandwidth
        ('fbw = gds / (2 * 3.14159 * (cdd + 20e-15))', ndim),
        # compute ro
        ('ro = 1.0 / gds', ndim),
        # set to maximum worst case gain
        ('obj = -min(gain)', 1),
    ]

    cons = dict(
        # constrain minimum bandwidth
        fbw=dict(lower=9e8),
    )

    # we can adjust vgs/vds over process corners.
    vector_params = {'vgs', 'vds'} if adj_bias else set()

    # minimize, set vbs = 0
    results = db.minimize(objective, define=define, cons=cons,
                          vector_params=vector_params, vbs=0, debug=debug)

    pprint.pprint(results)
