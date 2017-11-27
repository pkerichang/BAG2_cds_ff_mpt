# -*- coding: utf-8 -*-

import pprint

import bag
from abs_templates_ec.serdes import DynamicLatchChain
from bag.layout import RoutingGrid, TemplateDB

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

layers = [4, 5, 6]
spaces = [0.2, 0.2, 0.2]
widths = [0.1, 0.1, 0.1]
bot_dir = 'x'

routing_grid = RoutingGrid(prj.tech_info, layers, spaces, widths, bot_dir)

temp_db = TemplateDB('template_libs.def', routing_grid, impl_lib)
template = temp_db.new_template(params=layout_params, temp_cls=DynamicLatchChain, debug=True)
temp_db.instantiate_layout(prj, template, cell_name, debug=True)

