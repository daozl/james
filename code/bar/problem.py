#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from pkg import *
plt.figure(figsize=(12,6))
problem = ('Professional disagree',
		'Less employment information',
		'Lack of employment skills',
		'Do not understand the policy',
		'Personal orientation improperly',
		'Lack of social relations',
		'Lack of relevant work experience',
		'other')
x_pos = np.arange(len(problem))
performance = [41.28,43.12,44.04,26.61,22.02,16.51,54.13,0.92]

ret = plt.bar(x_pos,performance,0.35,color='b',align='center',alpha=0.8)
plt.xticks(x_pos,problem,rotation=-10)
plt.ylabel('percentage (%)')
plt.title('Employment problems')
autolabel(ret)
plt.show()
