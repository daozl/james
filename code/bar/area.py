#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from pkg import *

plt.figure(figsize=(12,8))
area = ['Dongbei',
		'Huabei',
		'Xibei',
		'Hua zhong',
		'Hua dong',
		'Hua nan',
		'Xi nan',
		'XiZang XinJiang']
#area.reverse()
y_pos = np.arange(len(area))
performance = [45.87,19.27,4.59,11.93,9.17,2.75,3.67,2.75]
#performance.reverse()
ret = plt.bar(y_pos,performance,0.35,color='g',align='center',alpha=0.8)
plt.xticks(y_pos,area)
plt.ylabel('percentage (%)')
plt.title('Areas of employment')
autolabel(ret)
plt.show()
