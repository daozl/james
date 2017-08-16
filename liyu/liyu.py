# -*- coding: utf-8 -*-

import networkx as nx					#导入复杂网络分析库，这个我也是第一次见到，不过网上有讲怎么用，我也学习了一下
import numpy as np						#numpy是数学计算计算的库
import random							#生成随机数的库
import matplotlib.pyplot as plt			#用来画图的库

M=1000
for theta in [2]:                       #for 循环，迭代列表[2] 其实也就一个元素2,这个for循环只是迭代了一次
    number=[]
    for c in [1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2]: # 第二个for循环。按顺序将列表中的值赋值给 c
        num=0
        for time in range(100):								#range(100) 函数会生成一个列表，里边的元素是 0 ～ 99
			G=nx.random_graphs.barabasi_albert_graph(M,2)	#生成一个n=1000，m=3的BA无标度网络
			#  print(theta)									#输出theta指向的值 也就是 2
			#  print(c)										#打印c指向的值
			
			
			W=[0 for i in G.nodes()]						#运用列表生成器，产生所有算素都为零的列表W
			for i in G.nodes():							
				W[i]=pow(G.degree(i),theta)                 #G.degree()返回某个节点的度 pow() 计算幂
			C=[0 for i in G.nodes()]                        #生成一个算素为节点的度与c指向的值的列表C
			for i in G.nodes():
				C[i]=c*W[i]
			F=[0 for i in G.nodes()]					#生成一个元素为节点的度的2次幂的列表F	
			for i in G.nodes():
				F[i]=W[i]
			
			n=0
			for i in G.nodes(): # 找出节点的度最大的节点 n 指向节点的值
				if G.degree(i)>G.degree(n):
					n=i
			LN=[]
			for i in G.edges(n):
				LN.append(i[1])
			UN=list(set(G.nodes())^set(LN)) 
			UN.remove(n)
			for k in range(10):
				#u=random.choice(UN)
				u=UN[0]
				for i in UN:
					if G.degree(i)>G.degree(n):
						u=i
				G.add_edge(n,u)
				UN.remove(u)
			m=1000
			WS=0
			for a in G.edges(n):
				WS=WS+W[a[1]]
			for a in G.edges(n):
				F[a[1]]=F[a[1]]+F[n]*W[a[1]]/WS
			G.remove_node(n)
			while nx.number_of_nodes(G)<m:
				m=nx.number_of_nodes(G)
				for n in G.nodes():
					if F[n]>C[n]:
						WS=0
						for a in G.edges(n):
							WS=WS+W[a[1]]
						for a in G.edges(n):
							F[a[1]]=F[a[1]]+F[n]*W[a[1]]/WS
						G.remove_node(n)
			    #print(nx.number_of_nodes(G))
			#print(nx.number_of_nodes(G))
			num=num+nx.number_of_nodes(G)
        number.append(num/100)
plt.plot(W,'b',label="hh")
plt.plot(C,'g',label="hl")
plt.plot(F,'r',label="hr")
plt.plot(UN,'y',label="no links")
plt.xlabel("tolerance number")
plt.ylabel("G")
plt.title("Comparison of Different Strategies by Adding 100 links")
plt.legend(loc='lower right')
plt.show()


