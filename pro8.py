# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 19:10:55 2019

@author: Administrator
"""

#输出9*9口诀

for i in range(1,10):
    for j in range(1,10):
        if i <= j:
            result = i * j
            print('%d * %d = %-3d'%(i,j,result), end = ' ')
        else:
            print('           ', end = ' ')
    print()