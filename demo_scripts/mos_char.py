# -*- coding: utf-8 -*-

import os

import bag
from serdes_bm.mos_char import AnalogMosCharacterization
from bag.layout import RoutingGrid, TemplateDB


def run_main(project):

    layout_params = dict(
        track_width=0.3e-6,
        track_space=0.4e-6,
        ptap_w=0.52e-6,
        ntap_w=0.52e-6,
        vm_layer='M3',
        hm_layer='M4',
        num_track_sep=0,
    )
    rcx_params = {'pexPexGroundNameValue': 'b'}
    impl_lib = 'mos_char_1'

    mos_type_list = ['nch', 'pch']
    l_list = [60e-9]
    w_list = [0.32e-6, 0.72e-6, 1.12e-6, 1.52e-6]
    intent_list = ['lvt', 'standard']
    env_list = ['tt', 'ff', 'ss', 'sf', 'fs', 'ss_hot', 'ff_hot']
    char_freq = 10e3
    vgs_abs = (0.0, 1.2, 41)
    vds_abs = (0.0, 1.2, 21)
    vbs_abs = (0.0, 1.0, 5)
    fg = 10
    fg_dum = 4

    layers = [4, 5, 6]
    spaces = [0.1, 0.1, 0.1]
    widths = [0.1, 0.1, 0.1]
    bot_dir = 'x'
    routing_grid = RoutingGrid(project.tech_info, layers, spaces, widths, bot_dir)
    temp_db = TemplateDB('template_libs.def', routing_grid, impl_lib)

    my_mos_char = AnalogMosCharacterization(project, os.path.abspath('mos_data'),
                                            impl_lib, 'mos_char', layout_params)

    sweep_attrs = dict(
        l=l_list,
        w=w_list,
        intent=intent_list,
    )

    for mos_type in mos_type_list:
        if mos_type == 'nch':
            sweep_params = dict(
                vgs=vgs_abs,
                vds=vds_abs,
                vbs=(-vbs_abs[1], -vbs_abs[0], vbs_abs[2]),
                )
        else:
            sweep_params = dict(
                vgs=(-vgs_abs[1], -vgs_abs[0], vgs_abs[2]),
                vds=(-vds_abs[1], -vds_abs[0], vds_abs[2]),
                vbs=vbs_abs,
                )

        constants = dict(
            mos_type=mos_type,
            fg=fg,
            fg_dum=fg_dum,
            char_freq=char_freq,
        )
        my_mos_char.simulate(temp_db, constants, sweep_attrs, sweep_params, env_list, 
                             extracted=True, rcx_params=rcx_params)

if __name__ == '__main__':
    print('creating BAG project')

    local_dict = locals()
    if 'prj' not in local_dict:
        prj = bag.BagProject()
    else:
        prj = local_dict['prj']

    run_main(prj)
