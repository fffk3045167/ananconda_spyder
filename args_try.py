# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 11:09:13 2019

@author: Administrator
"""

#支持任意参数形式的方法的一个应用点，就是实现对其他函数进行灵活调用。
"""
* 和 ** ，表示任意参数数目的收集
"""
def tracer(func, *args, **kargs):  
    print('calling', func.__name__)
    return func(*args, **kargs)
"""
* 和 ** 语法在函数调用中,表示解包参数集合
"""
def func(a,b,c,d):
    return a + b + c + d

print(tracer(func,1,2,c = 3,d = 4))