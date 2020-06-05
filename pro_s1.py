# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 13:52:59 2019

@author: Administrator
"""

"""
递归调用

"""

#计算阶乘
def fun_c(n):
    if n == 0:
        return 1  #0的阶乘等于1
    else:
        return n * fun_c(n - 1)  #递归调用

#计算累加
def fun_add(n):
    if n == 0:
        return 0
    else:
        return n + fun_add(n - 1)

if __name__ == '__main__':
    print(fun_c(5))
    print(fun_add(100))

