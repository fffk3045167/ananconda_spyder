# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 10:00:08 2019

@author: Administrator
"""

"""
高维数组的索引和分片
ndarray利用索引返回的低维数组子集也是视图而非拷贝，获取拷贝也需要显式的调用copy函数
"""

import numpy as np

#一维数组

arr1d = np.arange(10)
print(arr1d)
print(arr1d[5])
print(arr1d[2:4])

#二维数组

arr2d = np.arange(1,10).reshape((3,3))
print(arr2d[2])
print(arr2d[0,1])
print(arr2d[0][1])

#三维数组

arr3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr3d)
print(arr3d[0])
print(arr3d[0][1])
print(arr3d[0][1][1])

#高维数组切片

print(arr2d[:2,1:])

#切片索引混合使用

print(arr2d[:2,1])

#布尔索引

names = np.array(['tom','bob','bill','jack','tom'])

arr_bool = names == 'tom'
print(arr_bool)

data = np.random.randint(1,10,(5,3))

print(data)
print(data[arr_bool])
"""
bool型数组也是可以和切片、整数索引混用的
"""
print(data[arr_bool,1:])

#条件赋值

data[data < 3] = 0
print(data)

data[names == 'tom'] = 0
print(data)

#指定行与列的选取

arr = np.arange(32).reshape(8,4)

print(arr)
print(arr[[1,5,4,6]])  #选取第1、5、4、6行
print(arr[[1,5,4,6],[0,3,1,2]])   #选取第1、5、4、6行之后，再选取第0、3、1、2列
