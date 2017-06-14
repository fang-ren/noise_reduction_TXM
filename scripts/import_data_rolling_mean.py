"""
author: Fang Ren (SSRL)

6/8/2017
"""

import scipy.io
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from import_data import import_data

data = import_data()
for i in range(116):
    image = data[:,:,i]
    #print image.shape
    image = pd.rolling_mean(image, window = 3, center = True)
    image = image.T
    image = pd.rolling_mean(image, window = 3, center = True)
    image = image.T
    #print image.shape
    data[:, :, i] = image

save_path = '..\\report\\running_mean\\'
scipy.io.savemat(save_path+'9pixel_average.mat', {'imagestack':data})

vmin = np.nanmin(data)
vmax = np.nanmax(data)

selected = range(0, 116, 10)
plt.figure(1, figsize=(12,8))
for i in range(len(selected)):
    plt.subplot(3,4,i+1)
    plt.imshow(data[:,:,selected[i]])
    plt.clim(vmin, vmax)
    plt.tight_layout()


plt.savefig(save_path + '9pixel_average')

