# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 15:32:48 2019

@author: Administrator
"""

#动态类型与对象拷贝机制

list1 = [1,2,3,4,5]
list2 = list1[:]
list3 = [1,2,3,4,5]
list4 = list(list1)
print(list1 is list2)
print(list1 is list3)
print(list1 == list3)

print(list4)

str1 = 'what'
str2 = 'what'

print(str1 is str2)
"""
deepcopy自顶向下递归独立复制
实现自顶向下，深层次的将每一个层次的引用都做完整独立的复制
"""
import copy

list5 = [1,2,3,4]
list6 = [5,6,7,list5]

list7 = copy.deepcopy(list6)
list7[3][1] = [0]
print(list7)
print(list6)
print(list5)
