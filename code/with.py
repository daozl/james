# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt('/home/zldao/dao/python/my_data.txt')
    
plt.plot(data[:,0],data[:,1])
plt.show()