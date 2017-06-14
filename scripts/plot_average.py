"""
author: Fang Ren (SSRL)

6/13/2017
"""

from import_data import import_data
import numpy as np
import matplotlib.pyplot as plt
import scipy.io

energy = scipy.io.loadmat('..\\data\\energy.mat')['Es']
print energy.shape

data = import_data()
#print data.shape

data = np.sum(data, axis = 1)

#print data.shape

data = np.sum(data, axis = 0)

#print data.shape

plt.plot(energy,data)
plt.savefig('average.png')
