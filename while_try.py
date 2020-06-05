# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 13:28:35 2019

@author: Administrator
"""

#循环
a = 0
b = 10
'''
while a < b:
    print(a,end = ' ')
    a = a + 1

while a < b:
    a = a + 1
    if a % 2 != 0:
        continue
    print(a,end = ' ')
'''
while a < b:
    a = a + 1
    if a == 6:
        break
    print(a,end = ' ')

y = 33
#整除：//
x = y // 2
while x > 1:
    if y % x == 0:
        print('{} has a factor {}'.format(y,x))
        break
    x = x - 1
else:
    print('{} is prime'.format(y))