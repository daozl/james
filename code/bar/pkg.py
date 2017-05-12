# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
def autolabel(rets):
    """
    Attach a text label above each bar displaying its height
    """
    for ret in rets:
        height = ret.get_height()
        plt.text(ret.get_x() + ret.get_width()/2.,1.01*height,'%.2f' % float(height), ha = 'center',va = 'bottom')
