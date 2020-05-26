from bmtk.analyzer import nodes_table
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pdb
from mpl_toolkits.mplot3d import Axes3D
import h5py
from bmtk.analyzer.cell_vars import _get_cell_report, plot_report
import matplotlib.pyplot as plt
from scipy.signal import welch

# Load data
config_file = "simulation_config.json"
#lfp_file = "./output/ecp.h5"
mem_pot_file = './PN_IClamp/output/v_report.h5'
raster_file = './PN_IClamp/output/spikes.h5'
dt=0.1

# load 
i = h5py.File(mem_pot_file,'r')
r = h5py.File(raster_file,'r')


mem_potential = i['report']['mcortex']['data']
time = np.arange(0,dt*mem_potential.shape[0],dt)

plt.plot(time,mem_potential)



plt.show()

