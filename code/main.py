#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os

def fuc1():
	os.system("python bar/AreaLevel.py")



def funcerr():
    print "input error"

if __name__ == '__main__':
    while True:
        commond = raw_input("""请输入你关心的数据	
A 
B
C
D
E
F
G
H
I
G
K
L
M
N
O
P
Q
R
S
T
: """)
        if commond == 'A':
            fuc1()
        else:
            funcerr()
