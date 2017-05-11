#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(8,6))
grade = ()
x_pos = np.arange(len(grade))
performance = [4.59,23.85,32.11,39.45]

plt.bar(x_pos,performance,0.35,color='r',align='center',alpha=0.8)
plt.xticks(x_pos,grade)
plt.ylabel('percentage')
plt.title('The percentage of company')
plt.show()
