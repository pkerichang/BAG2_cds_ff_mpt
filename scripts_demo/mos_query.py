# -*- coding: utf-8 -*-

import pprint

import numpy as np
import matplotlib.pyplot as plt
# noinspection PyUnresolvedReferences
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib import ticker

from verification_ec.mos.query import MOSDBDiscrete

interp_method = 'spline'
spec_file = 'specs_char/nch_w4.yaml'
env_default = 'tt'
intent = 'standard'


def query(vgs=None, vds=None, vbs=0.0, vstar=None, env_list=None):
    """Get interpolation function and plot/query."""

    spec_list = [spec_file]
    if env_list is None:
        env_list = [env_default]

    # initialize transistor database from simulation data
    nch_db = MOSDBDiscrete(spec_list, interp_method=interp_method)
    # set process corners
    nch_db.env_list = env_list
    # set layout parameters
    nch_db.set_dsn_params(intent=intent)
    # returns a dictionary of smal-signal parameters
    return nch_db.query(vbs=vbs, vds=vds, vgs=vgs, vstar=vstar)


def plot_data(name='ibias', bounds=None, unit_val=None, unit_label=None):
    """Get interpolation function and plot/query."""
    env_list = [env_default]
    vbs = 0.0
    nvds = 41
    nvgs = 81
    spec_list = [spec_file]

    print('create transistor database')
    nch_db = MOSDBDiscrete(spec_list, interp_method=interp_method)
    nch_db.env_list = env_list
    nch_db.set_dsn_params(intent=intent)

    f = nch_db.get_function(name)
    vds_min, vds_max = f.get_input_range(1)
    vgs_min, vgs_max = f.get_input_range(2)
    if bounds is not None:
        if 'vgs' in bounds:
            v0, v1 = bounds['vgs']
            if v0 is not None:
                vgs_min = max(vgs_min, v0)
            if v1 is not None:
                vgs_max = min(vgs_max, v1)
        if 'vds' in bounds:
            v0, v1 = bounds['vds']
            if v0 is not None:
                vds_min = max(vds_min, v0)
            if v1 is not None:
                vds_max = min(vds_max, v1)

    # query values.
    vds_test = (vds_min + vds_max) / 2
    vgs_test = (vgs_min + vgs_max) / 2
    pprint.pprint(nch_db.query(vbs=vbs, vds=vds_test, vgs=vgs_test))

    vbs_vec = [vbs]
    vds_vec = np.linspace(vds_min, vds_max, nvds, endpoint=True)
    vgs_vec = np.linspace(vgs_min, vgs_max, nvgs, endpoint=True)
    vbs_mat, vds_mat, vgs_mat = np.meshgrid(vbs_vec, vds_vec, vgs_vec, indexing='ij', copy=False)
    arg = np.stack((vbs_mat, vds_mat, vgs_mat), axis=-1)
    ans = f(arg)

    vds_mat = vds_mat.reshape((nvds, nvgs))
    vgs_mat = vgs_mat.reshape((nvds, nvgs))
    ans = ans.reshape((nvds, nvgs, len(env_list)))

    formatter = ticker.ScalarFormatter(useMathText=True)
    formatter.set_scientific(True)
    formatter.set_powerlimits((-2, 3))
    if unit_label is not None:
        zlabel = '%s (%s)' % (name, unit_label)
    else:
        zlabel = name
    for idx, env in enumerate(env_list):
        fig = plt.figure(idx + 1)
        ax = fig.add_subplot(111, projection='3d')
        cur_val = ans[..., idx]
        if unit_val is not None:
            cur_val = cur_val / unit_val
        ax.plot_surface(vds_mat, vgs_mat, cur_val, rstride=1, cstride=1, linewidth=0, cmap=cm.cubehelix)
        ax.set_title('%s (corner=%s)' % (name, env))
        ax.set_xlabel('Vds (V)')
        ax.set_ylabel('Vgs (V)')
        ax.set_zlabel(zlabel)
        ax.w_zaxis.set_major_formatter(formatter)

    plt.show()
