# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#list

list1 = [1,2,3,4,5,6,7,8,9]
list2 = [2,'sum',[4,6,8]]
list3 = []

#切片,左闭右开
print(list1[1:3])
print(list1[1:])
print(list1[:3])
print(list1[3:-1])
print(list1[0::2])

#添加
list1.append(10)
print(list1)

list1.insert(1,1.5)
print(list1)

list1.extend([11,12,13])
print(list1)

#删除
list4 = ['a','b','b','c']

list4.remove('a')
print(list4)

del list4[0:1]
print(list4)

list4.pop()
print(list4)

#修改
list5 = [3,4,5,6,7,8]
list5[0] = ['a']
list5[1:2] = ['b','c','d']

#排序
list6 = [1,2,3,4,5,6,7]
list6.sort()
print(list6)
list6.reverse()
print(list6)