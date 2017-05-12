#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from pkg import *
plt.figure(figsize=(8,6))
reason = ('Unilateral employment',
		'Low wages in the industry',
		'Knowledge can not meet the requirements of work',
		'Institutional and immature',
		'other')
x_pos = np.arange(len(reason))
performance = [14.68,8.26,66.06,9.17,1.83]

ret = plt.bar(x_pos,performance,0.35,color='b',align='center',alpha=0.8)
plt.xticks(x_pos,reason,rotation=-15)
plt.ylabel('percentage (%)')
plt.title('Work and professional does not match the reasons')
autolabel(ret)
plt.show()
