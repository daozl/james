#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from pkg import *
plt.figure(figsize=(12,8))
company = ['Party organs','Institutions','State-owned enterprises',
			'Non-state enterprises','Basic project','Independent business',
			'Flexible employment','Social work organization','Freelance','other']
#company.reverse()
y_pos = np.arange(len(company))
performance = [5.5,17.43,11.93,44.04,6.42,4.59,3.67,0.92,4.59,0.92]
#performance.reverse()
ret = plt.bar(y_pos,performance,0.35,color='r',align='center',alpha=0.8)
plt.xticks(y_pos,company,rotation=-12)
plt.ylabel('percentage (%)')
plt.title('Work Type')
autolabel(ret)
plt.show()
