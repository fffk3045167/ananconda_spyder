# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 19:18:32 2019

@author: Administrator
"""

"""
可迭代对象支持内置函数iter，通过对可迭代对象调用iter函数，会返回一个迭代器，
而“迭代器”支持内置函数next，通过不断对其调用next方法，会依次前进到序列中的下一个元素并将其返回，
最后到达一系列结果的末尾时，会引发StopIteration异常。
对迭代器调用iter方法，则会返回迭代器自身。
"""

list1 = [1,2,3]

i = iter(list1)
print(i)
print(list1 is i)
print(i is iter(i))