# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 15:16:59 2019

@author: Administrator
"""

for line in open ('testfile.txt', 'r'):
    print(line, end = '  ')

#三种循环迭代方法:range zip enumerate

for x in range(5):
    print(x, end = ' ')
    
print(range(6))

l1 = ['a','b','c']
l2 = [1,2,3]
for x in zip(l1,l2):
    print(x, end = ' ')

D = dict(zip(l1,l2))
print(D)

k = 'anaconda3'
for x in enumerate(k):
    print(x, end = ' ')

"""
列表解析式
    1、输入序列的运算表达式
    2、对输入序列的循环表达式
    3、对输入序列的过滤条件（非必须）
"""
a = [1,2,3,4,5,6,7,8,9,10]
"""
    1:x**2
    2:for x in a
    3:if x % 2 == 0
"""
b = [x**2 for x in a if x % 2 == 0]
print(b)

"""
字典解析式
"""
"""
    1、字典构造字典
"""
dic1 = {'a': 1,'b': 2,'c': 3,'d': 4}
dic2 = {k: v**2 for (k, v) in dic1.items()}
print(dic2)

"""
    2、列表构造字典
"""

dic3 = {c: c*4 for c in ['q','w','e','r']}
print(dic3)