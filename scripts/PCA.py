"""
author: Fang Ren (SSRL)

6/13/2017
"""


from import_data import import_data
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA
import scipy.io

#data = import_data(path = '..\\report\\running_mean\\9pixel_average.mat')
data = import_data()
data = np.nan_to_num(data)
height, width, depth = data.shape
#print height, width, depth
data_flat = data.reshape((height*width, depth))
#print data_flat.shape

# print data_flat[5,:] == data[0,5,:]
# print data_flat[764,:] == data[1,0,:]

num_of_components = 10

pca = PCA(n_components = num_of_components, svd_solver= 'full')
pca.fit(data_flat)
components = pca.components_
weights = pca.transform(data_flat)
#ratio = pca.explained_variance_ratio_
num_of_components = components.shape[0]
mu = np.mean(data_flat, axis=0)

print components.shape, weights.shape, weights

import scipy.io

energy = scipy.io.loadmat('..\\data\\energy.mat')['Es']
print energy.shape


save_path = '..\\report\\pca\\'

for i in range(num_of_components):
    plt.title('component' + str(i+1))
    plt.plot(energy, components[i,:])
    plt.savefig(save_path + 'component' + str(i+1) + '.png')
    plt.close('all')


weight = weights[:,:1]
component = components[:1,:]
print weight.shape, component.shape

component1 = np.dot(weight, component)
component1 += mu

component1 = component1.reshape((height, width, depth))
scipy.io.savemat(save_path + 'component1.mat', {'component1':component1})

data = component1
vmin = np.nanmin(data)
vmax = np.nanmax(data)
selected = range(0, 116, 10)
plt.figure(1, figsize=(12,8))

for i in range(len(selected)):
    plt.subplot(3,4,i+1)
    plt.title('component1')
    plt.imshow(data[:,:,selected[i]])
    plt.clim(vmin, vmax)
    plt.tight_layout()

plt.savefig(save_path + 'image_component1.png')
plt.close('all')

