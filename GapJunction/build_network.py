from bmtk.builder.networks import NetworkBuilder
import numpy as np
import synapses

synapses.load()

net = NetworkBuilder('mcortex')
net.add_nodes(N=1,cell_name='cell1',
              potental='exc',
              model_type='biophysical',
              model_template='hoc:stylized_typeC',
              morphology=None
              )

net.add_nodes(N=1,cell_name='cell2',
              potental='exc',
              model_type='biophysical',
              model_template='hoc:stylized_typeC',
              morphology=None
              )


#net.add_edges(source={'cell_name': 'cell1'}, target={'cell_name': 'cell2'},
#                   connection_rule=1,
#                   syn_weight=0.001,
#                   delay=2.0,
#                   weight_function=None,
#                   target_sections=['somatic'],
#                   distance_range=[0.0, 150.0],
#                   dynamics_params='AMPA_ExcToExc.json',
#                   model_template='exp2syn')


gap_conn = net.add_edges(source={'cell_name': 'cell1'}, target={'cell_name': 'cell2'},
              connection_rule=1,
              syn_weight=1,
              dynamics_params='GAP.json',
              model_template='Gap',
              distance_range=[0.0, 300.0],
              target_sections=['somatic'])
#
#gap_conn.add_properties('IsGapJunction',True)

net.build()
net.save_nodes(output_dir='network')
net.save_edges(output_dir='network')

from bmtk.utils.sim_setup import build_env_bionet

build_env_bionet(base_dir='GAP_IClamp',      # Where to save the scripts and config files 
                 components_dir='components',
                 network_dir='network',    # Location of directory containing network files
                 tstop=2000.0, dt=0.1,     # Run a simulation for 2000 ms at 0.1 ms intervals
                 report_vars=['v'], # Tells simulator we want to record membrane potential and calcium traces
                 current_clamp={           # Creates a step current from 500.ms to 1500.0 ms  
                     'amp': 0.1,
                     'delay': 500.0,
                     'duration': 1000.0,
                     'gids': 0
                 },
                 compile_mechanisms=True   # Will try to compile NEURON mechanisms
                )
                
