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
edge_file = './network/mcortex_mcortex_edges.h5'

# load 
f = h5py.File(edge_file,'r')

pdb.set_trace()
