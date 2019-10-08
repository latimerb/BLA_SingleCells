from bmtk.builder.networks import NetworkBuilder

net = NetworkBuilder('mcortex')
net.add_nodes(N=10,cell_name='Scnn1a_473845048',
              potental='exc',
              model_type='biophysical',
              model_template='hoc:stylized_typeC',
              morphology=None
              )

net.build()
net.save_nodes(output_dir='network')

for node in net.nodes():
    print(node)
    
from bmtk.utils.sim_setup import build_env_bionet

build_env_bionet(base_dir='PN_IClamp',      # Where to save the scripts and config files 
                 components_dir='components',
                 network_dir='network',    # Location of directory containing network files
                 tstop=2000.0, dt=0.1,     # Run a simulation for 2000 ms at 0.1 ms intervals
                 report_vars=['v'], # Tells simulator we want to record membrane potential and calcium traces
                 current_clamp={           # Creates a step current from 500.ms to 1500.0 ms  
                     'amp': 0.009,
                     'delay': 500.0,
                     'duration': 1000.0
                 },
                 compile_mechanisms=True   # Will try to compile NEURON mechanisms
                )
                
