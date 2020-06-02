import numpy as np
import matplotlib.pyplot as plt
import pdb
import pandas as pd

Fs =  10000
f = 5
sample = 100000
x = np.arange(sample)
y = 0*np.sin(2 * np.pi * f * (x / Fs))

plt.plot(x,y)
plt.show()

df = pd.DataFrame(y)
df.to_csv('./PN_IClamp/components/templates/5Hz_nonoise.csv',index=False)
