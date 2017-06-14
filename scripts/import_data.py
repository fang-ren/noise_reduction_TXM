"""
author: Fang Ren (SSRL)

6/8/2017
"""

import scipy.io

def import_data(path = '..\\data\\data.mat'):
    data = scipy.io.loadmat(path)['imagestack']
    print data.shape
    return data

# data = import_data()