import numpy as np
import pprint

import bag
from invamp_layout.core import InvAmp
from bag.layout import RoutingGrid, TemplateDB

impl_lib = 'AAAFOO2'
cell_name = 'invamp'
tb_lib = 'invamp_testbenches'
tb_cell = 'invamp_tb_ac'
cload = 20e-15
vbias_best = 0.5
vdd = 1.0

def generate(prj, temp_db):
    global vbias_best
    params = dict(
        lch=60e-9,
        w=0.55e-6,
        intent='lvt',
        ndum=4,
        cload=cload,
        f_targ=5e9,
        vdd=vdd,
    )
    layout_params = dict(
        ptap_w=1e-6,
        ntap_w=1e-6,
        io_width_ntr=2,
    )
    lib_name = 'invamp_templates'

    print('designing module')
    dsn = prj.create_design_module(lib_name, cell_name)
    vbias_best = dsn.design(**params)
    dsn.implement_design(impl_lib, top_cell_name=cell_name, erase=True)
    layout_params = dsn.get_layout_params(**layout_params)
    pprint.pprint(layout_params)
    template = temp_db.new_template(params=layout_params, temp_cls=InvAmp, debug=True)
    temp_db.instantiate_layout(prj, template, cell_name, debug=True)


def extract(prj):
    print('running lvs')
    lvs_passed, lvs_log = prj.run_lvs(impl_lib, cell_name)
    if not lvs_passed:
        raise Exception('oops lvs died.  See LVS log file %s' % lvs_log)
    print('lvs passed')

    # run rcx
    print('running rcx')
    rcx_passed, rcx_log = prj.run_rcx(impl_lib, cell_name)
    if not rcx_passed:
        raise Exception('oops rcx died.  See RCX log file %s' % rcx_log)
    print('rcx passed')


def simulate(prj):
    tb = prj.create_testbench(tb_lib, tb_cell, impl_lib, cell_name, impl_lib)
    print('setting testbench parameters')
    tb.set_parameter('cload', cload)
    tb.set_parameter('vbias', vbias_best)
    tb.set_parameter('vdd', vdd)

    tb.set_simulation_environments(['tt'])
    # tb.add_output('outac', """getData("/outac" ?result 'tran)""")

    tb.set_simulation_view(impl_lib, cell_name, 'calibre')

    tb.update_testbench()
    print('running simulation')
    tb.run_simulation()

    print('loading results')
    results = bag.data.load_sim_results(tb.save_dir)

    import matplotlib.pyplot as plt

    plt.figure(1)
    xvec = results['freq']
    yvec = results['vout_ac']
    plt.loglog(xvec, np.abs(yvec))

    plt.figure(2)
    xvec = results['vbias']
    yvec = results['vout_dc']
    plt.plot(xvec, yvec)

    plt.show()

if __name__ == '__main__':
    local_dict = locals()
    if 'bprj' not in local_dict:
        print('creating BAG project')
        bprj = bag.BagProject()
        temp = 70.0
        layers = [4, 5, 6]
        spaces = [0.1, 0.1, 0.1]
        widths = [0.1, 0.1, 0.1]
        bot_dir = 'x'

        routing_grid = RoutingGrid(bprj.tech_info, layers, spaces, widths, bot_dir)

        tdb = TemplateDB('template_libs.def', routing_grid, impl_lib)
    else:
        print('loading BAG project')
