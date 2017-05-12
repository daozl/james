#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(12,8))
area = ['Dongbei',
		'Huabei',
		'Xibei',
		'Hua zhong',
		'Hua dong',
		'Hua nan',
		'Xi nan',
		'XiZang XinJiang']
area.reverse()
y_pos = np.arange(len(area))
performance = [45.87,19.27,4.59,11.93,9.17,2.75,3.67,2.75]
performance.reverse()
plt.barh(y_pos,performance,0.35,color='g',align='center',alpha=0.8)
plt.yticks(y_pos,area)
plt.xlabel('percentage (%)')
plt.title('Areas of employment')
plt.show()
