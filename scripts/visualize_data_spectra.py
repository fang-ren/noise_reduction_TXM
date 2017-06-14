"""
author: Fang Ren (SSRL)

6/8/2017
"""

from import_data import import_data
import matplotlib.pyplot as plt
import numpy as np
import scipy.io

#data = import_data()
data = scipy.io.loadmat('..\\report\\component1\\component1_7pixel.mat')['component1']
print data.shape

vmin = np.nanmin(data)
vmax = np.nanmax(data)

x, y = np.meshgrid(range(0,data.shape[0], 100), range(0,data.shape[1], 100))
grids = x.shape
x = x.flatten()
y = y.flatten()
#print x, y

import scipy.io

energy = scipy.io.loadmat('..\\data\\energy.mat')['Es']
print energy.shape


plt.figure(1, figsize=(15, 7))
for i in range(len(x)):
    plt.subplot(grids[1],grids[0],i+1)
    #print x[i],y[i]
    plt.plot(energy,data[x[i],y[i],:], label = str(x[i]) + ',' + str(y[i]))
    plt.legend(fontsize = 5)
    plt.tight_layout()
    #plt.ylim(2, 2.6)
    plt.xticks([])
    #plt.yticks([])

# save_path = '..\\report\\spectrum_visualization\\'
# plt.savefig(save_path + 'spectrum', dpi = 600)


save_path = '..\\report\\component1\\'
plt.savefig(save_path + 'component1_7pixel_spectra')

