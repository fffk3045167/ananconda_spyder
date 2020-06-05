# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 14:55:25 2020

@author: Administrator
"""

"""
列表并行排序
"""

list1 = [5, 2, 4]
list2 = [2, 6, 9]
"""
zip() 函数用于将可迭代的对象作为参数，
将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，
利用 * 号操作符，可以将元组解压为列表。
"""
data = list(zip(list1, list2))
data.sort()
list1, list2 = map(lambda t: list(t), zip(*data))
print('list1 = {}\nlist2 = {}\ndata = {}'.format(list1,list2,data))
"""
output：
list1 = [2, 4, 5]
list2 = [6, 9, 2]
data = [(2, 6), (4, 9), (5, 2)]
"""