#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt
#import numpy as np

#data = np.loadtxt('/home/zldao/dao/python/my_data.txt')

#调节图形的大小，宽，高
plt.figure(figsize=(12,16))

#定义饼状图的标签，标签是列表
labels = ['Internship','graduation','Graduated within three months',
      'Graduated within six months','Graduated within 1 year']

#每个标签占多大，会自动计算百分比
sizes = [45.87,28.44,15.6,9.17,0.92]

#将某部分爆炸出来，使用括号，将第一块分割出来，数值的大小是分割出来的与剩下的间隙
explode = (0,0,0,0,0.05)

patches,l_text,p_text = plt.pie(sizes,explode = explode,
                                 labels = labels,colors = None,
                                 labeldistance = 1.1 ,autopct = '%4.2f%%',
                                 shadow = False,startangle = 90,pctdistance = 0.6)
#labeldistance,文本的位置离圆点有多远，1.1指1.1倍半径的位置
#autopct，圆里面的文本格式,%4.2f%%表示小数有三位，整数有两位的浮点数
#shadow，饼是否有阴影
#startangle,起始角度，0,表示从0开始逆时针转，为第一块。一般选择从90度开始比较好看
#pcdistance，百分比的text离圆心的距离
#patches，l_texts,p_texts,为了得到饼状图的返回值，p_texts饼图内部文本的，l_texts饼外部文本

#改变文本的大小
#方法是把每一个text遍历。调用set_size方法设置它的属性
for t in l_text:
    t.set_size(15)
for t in p_text:
    t.set_size(15)
#plt.title('The proportion of men and women',fontsize=20,loc='center')
#设置x,y轴刻度一致，这样饼图才能是圆的
plt.axis('equal')
plt.legend()
plt.show()
