#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(8,6))
consistent = ('complete match','basically consistent',
			'a little contact', 'does not match')
x_pos = np.arange(len(consistent))
performance = [4.59,31.19,46.79,17.43]

plt.bar(x_pos,performance,0.35,color='r',align='center',alpha=0.8)
plt.xticks(x_pos,consistent)
plt.ylabel('percentage (%)')
plt.title('Work and professional consistency')
plt.show()
