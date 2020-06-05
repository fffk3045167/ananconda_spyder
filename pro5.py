# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 13:59:31 2019

@author: Administrator
"""
#输入三个整数x,y,z，请把这三个数由小到大输出。
import random
list1 = [None] * 3

print(random.randint(5,10))

for x in range(3):
    list1[x] = random.randint(100,500)

print(list1)
if list1[0] >= list1[1]:
    n = list1[0]
    list1[0] = list1[1]
    list1[1] = n
    if list1[1] >= list1[2]:
        n = list1[1]
        list1[1] = list1[2]
        list1[2] = n
        if list1[0] >= list1[1]:
            n = list1[0]
            list1[0] = list1[1]
            list1[1] = n
elif list1[0] < list1[1]:
    if list1[1] >= list1[2]:
        n = list1[1]
        list1[1] = list1[2]
        list1[2] = n
        if list1[0] >= list1[1]:
            n = list1[0]
            list1[0] = list1[1]
            list1[1] = n
            
list1.sort()
print(list1)

