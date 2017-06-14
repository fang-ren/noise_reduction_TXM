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
print vmax, vmin

selected = range(0, 116, 10)
plt.figure(1, figsize=(12,8))
for i in range(len(selected)):
    plt.subplot(3,4,i+1)
    plt.imshow(data[:,:,selected[i]])
    plt.clim(1.76961530414, 2.89950014014)
    plt.tight_layout()


save_path = '..\\report\\component1\\'
plt.savefig(save_path + 'component1_7pixel')
