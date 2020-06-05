# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 14:03:30 2019

@author: Administrator
"""
"""
try/except的组合可用于捕捉异常并从中恢复，
try/finally的组合则很方便，可以确保无论try代码块内的代码是否发生了异常，终止行为都一定会运行。
"""
#主动捕获异常
def test(obj, index):
    return obj[index]

x = 'qwer'

try:
    test(x,6)
except  IndexError:
    print('主动捕获成功')

#主动触发异常

try:
    raise IndexError
except IndexError:
    print('主动触发，捕获成功')
    

#自定义异常

class Bad(Exception):
    pass
def dome():
    raise Bad()

try:
    dome()
except Bad:
    print('自定义的异常')

#finally定义收尾行为

try:
    raise IndexError
finally:
    print('无论是否异常，一定运行')

print('test')

"""
把捕捉到的异常对象赋予了e这个变量名，可以方便的访问异常实例的数据以及异常类中的方法。
"""
try:
    pass
except IndexError as e:
    print(e.args)