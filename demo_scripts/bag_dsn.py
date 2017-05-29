# -*- coding: utf-8 -*-
import bag
import matplotlib.pyplot as plt
import pprint


lib_name = 'demo_templates'
cell_name = 'gm'
impl_lib = 'demo_1'
tb_lib = 'demo_testbenches'
tb_cell = 'gm_tb_tran'
plot_wvfm = 'outac'

params = dict(
    lch=18e-9,
    win=4,
    wt=4,
    nf=4,
    ndum_extra=2,
    input_intent='fast',
    tail_intent='standard',
)

print('creating BAG project')
prj = bag.BagProject()

# create design module and run design method.
print('designing module')
dsn = prj.create_design_module(lib_name, cell_name)
print('design parameters:\n%s' % pprint.pformat(params))
dsn.design(**params)

# implement the design
print('implementing design with library %s' % impl_lib)
dsn.implement_design(impl_lib, top_cell_name=cell_name, erase=True)

#dsn.update_structure()
#prj.implement_design(impl_lib, dsn)

# create testbench
print('creating testbench %s__%s' % (impl_lib, tb_cell))
tb = prj.create_testbench(tb_lib, tb_cell, impl_lib, cell_name, impl_lib)

print('setting testbench parameters')
tb.set_parameter('tsim', 3e-9)
tb.set_parameter('rload', 1000)
tb.set_parameter('tper', 250e-12)
tb.set_parameter('tr', 15e-12)
tb.set_parameter('vamp', 120e-3)
tb.set_parameter('vbias', 0.45)
tb.set_parameter('vcm', 0.7)
tb.set_parameter('vdd', 1.0)
tb.set_parameter('tstep', 1e-12)
tb.set_sweep_parameter('cload', values=[5e-15, 20e-15, 100e-15])

tb.set_simulation_environments(['tt', 'ff'])

tb.add_output(plot_wvfm, """getData("/OUTAC" ?result 'tran)""")

print('committing testbench changes')
tb.update_testbench()

print('running simulation')
tb.run_simulation()

print('loading results')
results = bag.data.load_sim_results(tb.save_dir)

print('output waveforms: %s' % results.keys())
vout = results[plot_wvfm]

print('%s sweep parameters: %s' % (plot_wvfm, vout.sweep_params))

par1 = vout.sweep_params[0]
par2 = vout.sweep_params[1]
idx1 = -1
idx2 = -1
print('plotting waveform with parameters:')
print('%s = %s' % (par1, results[par1][idx1]))
print('%s = %s' % (par2, results[par2][idx2]))
tvec = results['time']
vvec = vout[idx1, idx2, :]

plt.figure(1)
plt.plot(tvec, vvec)
plt.show(block=False)
