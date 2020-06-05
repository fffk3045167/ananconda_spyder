# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 20:01:04 2019

@author: Administrator
"""

#打印出100-999之间所有的水仙花数

for n in range(100, 999):
    i = int(n / 100)
    j = int(n / 10 % 10)
    k = int(n % 10)
    if n == i ** 3 + j ** 3 + k ** 3:
        print(n)