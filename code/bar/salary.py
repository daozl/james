#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(8,6))
salary = ('1500 or less','1500-3000','3000-4500','4500-6000','6000 or more')
x_pos = np.arange(len(salary))
first = [13,74,15,5,2]
current = [3,34,38,19,15]
ret1 = plt.bar(x_pos-0.1,first,0.2,color='b',alpha=0.8,label='first salary')
ret2 = plt.bar(x_pos+0.1,current,0.2,color='r',alpha=0.8,label='current salary')
plt.xticks(x_pos,salary)
plt.ylabel('The number of people')
plt.title('First salary and current salary')
plt.legend((ret1[0],ret2[0]),('first salary','current salary'))
def autolabel(rets):
    """
    Attach a text label above each bar displaying its height
    """
    for ret in rets:
        height = ret.get_height()
        plt.text(ret.get_x() + ret.get_width()/2.,1.01*height,'%d' % int(height), ha = 'center',va = 'bottom')
autolabel(ret1)
autolabel(ret2)
plt.show()
