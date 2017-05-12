#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from pkg import *

plt.figure(figsize=(12,9))
area = ['Capital cities and municipalities',
		'Developed cities in the province',
		'Other cities in the province',
		'County or county',
		'Township']

#area.reverse()
y_pos = np.arange(len(area))
performance = [47.69,21.1,23.58,5.5,2.73]
#performance.reverse()
ret = plt.bar(y_pos,performance,0.35,color='g',align='center',alpha=0.8)
plt.xticks(y_pos,area,rotation=-10)
plt.ylabel('percentage (%)')
plt.title('Employer area')
autolabel(ret)
plt.show()
