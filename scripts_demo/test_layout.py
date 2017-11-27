# -*- coding: utf-8 -*-

import pprint

import bag
from abs_templates_ec.serdes import DynamicLatchChain
# from templates_tsmc16.AnalogGuardRingTSMC16 import AnalogGuardRingTSMC16
from bag.layout import RoutingGrid, TemplateDB

impl_lib = 'AAAFOO'


def diffamp(prj, temp_db, gnf=2):
    lib_name = 'serdes_bm_templates'
    cell_name = 'diffamp_en_casc'

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

    # create design module and run design method.
    print('designing module')
    dsn = prj.create_design_module(lib_name, cell_name)
    print('design parameters:\n%s' % pprint.pformat(params))
    dsn.design_specs(**params)

    layout_params = dict(
        ptap_w=0.5e-6,
        ntap_w=0.5e-6,
        track_width=0.1e-6,
        track_space=0.1e-6,
        gds_space=1,
        diff_space=1,
        ng_tracks=[1, 1, 1, 3, 1],
        nds_tracks=[1, 1, 1, 1, 1],
        pg_tracks=1,
        pds_tracks=3,
        vm_layer='M3',
        hm_layer='M4',
        guard_ring_nf=gnf,
    )

    layout_params = dsn.get_layout_params(**layout_params)
    pprint.pprint(layout_params)

    template = temp_db.new_template(params=layout_params, temp_cls=DynamicLatchChain, debug=True)
    temp_db.instantiate_layout(prj, template, cell_name, debug=True)

def guardring(prj, temp_db, height=20):
    cell_name = 'guardring'
    layout_params = dict(
        lch=16e-9,
        height=height,
        sub_type='ptap',
        threshold='ulvt',
        fg=4,
        is_corner=False,
    )

    template = temp_db.new_template(params=layout_params, temp_cls=AnalogGuardRingTSMC16, debug=True)
    temp_db.instantiate_layout(prj, template, cell_name, debug=True)
    
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
