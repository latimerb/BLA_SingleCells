from bmtk.builder.networks import NetworkBuilder

net = NetworkBuilder('mcortex')
net.add_nodes(N=1,cell_name='PN',
              potental='exc',
              model_type='biophysical',
              model_template='hoc:stylized_typeC',
              morphology=None
              )

net.add_nodes(N=1,cell_name='Chn',
              potental='exc',
              model_type='biophysical',
              model_template='hoc:chandelierWB',
              morphology=None
              )

conn = net.add_edges(source=net.nodes(cell_name='Chn'), target=net.nodes(cell_name='PN'),
                   connection_rule=1,
                   syn_weight=0.009,
                   weight_function=None,
                   target_sections=['axonal'],
                   delay=0.0,
                   distance_range=[0.0, 300.0],
                   dynamics_params='GABA_InhToExc.json',
                   model_template='Exp2Syn')

net.build()
net.save_nodes(output_dir='network')
net.save_edges(output_dir='network')

for node in net.nodes():
    print(node)

for edge in net.edges():
    print(edge)
    
from bmtk.utils.sim_setup import build_env_bionet

build_env_bionet(base_dir='PN_IClamp',      # Where to save the scripts and config files 
                 components_dir='components',
                 network_dir='network',    # Location of directory containing network files
                 tstop=10000.0, dt=0.1,     # Run a simulation for 2000 ms at 0.1 ms intervals
                 report_vars=['v'], # Tells simulator we want to record membrane potential and calcium traces
                 current_clamp={           # Creates a step current from 500.ms to 1500.0 ms  
                     'amp': [0.0,0.0000029],
                     'delay': [200,800],
                     'duration': [1000,19200],
                     'gids':[0,1]
                 },
                 compile_mechanisms=True   # Will try to compile NEURON mechanisms
                )
                
