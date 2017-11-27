# -*- coding: utf-8 -*-

import pprint

import bag
from abs_templates_ec.serdes import DynamicLatchChain
from bag.layout import RoutingGrid, TemplateDB

lib_name = 'serdes_bm_templates'
cell_name = 'diffamp_en_casc'
impl_lib = 'serdes_bm_1'
tb_lib = 'serdes_bm_testbenches'
tb_cell = 'diffamp_en_casc_tb_tran'
do_layout = True
run_lvs = True
run_rcx = True

params = dict(
    lch=60e-9,
    pw=0.72e-6,
    pfg=6,
    nw_list=[0.52e-6, 0.72e-6, 0.52e-6, 0.72e-6],
    nfg_list=[4, 6, 4, 6],
    nduml=3,
    ndumr=3,
    nsep=2,
    input_intent='standard',
    tail_intent='lvt',
    device_intent='lvt',
    )

layout_params = dict(
    ptap_w=1.0e-6,
    ntap_w=1.0e-6,
    gds_space=1,
    diff_space=1,
    ng_tracks=[1, 1, 1, 3, 1],
    nds_tracks=[1, 1, 1, 1, 1],
    pg_tracks=1,
    pds_tracks=3,
)

print('creating BAG project')
prj = bag.BagProject()

# create design module and run design method.
print('designing module')
dsn = prj.create_design_module(lib_name, cell_name)
print('design parameters:\n%s' % pprint.pformat(params))
dsn.design_specs(**params)

# implement the design
print('implementing design with library %s' % impl_lib)
dsn.implement_design(impl_lib, top_cell_name=cell_name, erase=True)
layout_params = dsn.get_layout_params(**layout_params)

pprint.pprint(layout_params)

if do_layout:
    # create layout
    layers = [4, 5, 6]
    spaces = [0.2, 0.2, 0.2]
    widths = [0.1, 0.1, 0.1]
    bot_dir = 'x'

    routing_grid = RoutingGrid(prj.tech_info, layers, spaces, widths, bot_dir)

    temp_db = TemplateDB('template_libs.def', routing_grid, impl_lib)
    template = temp_db.new_template(params=layout_params, temp_cls=DynamicLatchChain, debug=True)
    temp_db.instantiate_layout(prj, template, cell_name, debug=True)

    # run lvs
    if run_lvs:
        print('running lvs')
        lvs_passed, lvs_log = prj.run_lvs(impl_lib, cell_name)
        if not lvs_passed:
            raise Exception('oops lvs died.  See LVS log file %s' % lvs_log)
        print('lvs passed')

    if run_rcx:
        # run rcx
        print('running rcx')
        rcx_passed, rcx_log = prj.run_rcx(impl_lib, cell_name)
        if not rcx_passed:
            raise Exception('oops rcx died.  See RCX log file %s' % rcx_log)
        print('rcx passed')

if not do_layout or (run_lvs and run_rcx):
    # setup testbench
    print('creating testbench %s__%s' % (impl_lib, tb_cell))
    tb = prj.create_testbench(tb_lib, tb_cell, impl_lib, cell_name, impl_lib)

    print('setting testbench parameters')
    tb.set_parameter('cload', 10e-15)
    tb.set_parameter('vcasc', 1.0)
    tb.set_parameter('vdd', 1.0)
    tb.set_parameter('vin_amp', 0.02)
    tb.set_parameter('vin_freq', 5e9)
    tb.set_parameter('vindc', 0.7)
    tb.set_parameter('vload', 0.4)
    tb.set_parameter('vtail', 0.5)
    tb.set_parameter('tsim', 1e-9)
    tb.set_parameter('tstep', 0.5e-12)

    tb.set_simulation_environments(['tt'])
    tb.add_output('outac', """getData("/outac" ?result 'tran)""")

    if do_layout:
        tb.set_simulation_view(impl_lib, cell_name, 'calibre')

    tb.update_testbench()

    print('running simulation')
    tb.run_simulation()

    print('loading results')
    results = bag.data.load_sim_results(tb.save_dir)

    tvec = results['time']
    yvec = results['outac']

    import matplotlib.pyplot as plt

    plt.figure(1)
    plt.plot(tvec, yvec)
    plt.show(block=False)
