# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 14:59:03 2019

@author: Administrator
"""

import numpy as np

data = [1,2.32,4,32]
arr = np.array(data)
print(arr)
print(type(arr))

"""
获取多维数组的基本属性：维数、形状和判定合适的数据类型
"""

data = [[1,2,3,4],[5,6,7,8.2]]
arr = np.array(data)

print(arr)
#数组的维数  data.ndim = len(data.shape)
print(arr.ndim)
#形状,即行列数
print(arr.shape)
#数据类型
print(arr.dtype)
print(type(arr))

"""
不仅在初始化数组时可以指定数据类型，同时可以对已有的ndarray数组进行数据类型的显式转换。
"""
arr1 = np.array([1,2,3,4], dtype = np.float64)
arr2 = np.array([1,2,3,4], dtype = np.int32)
"""
通过astype进行数据类型的显示转换，创建一个新的数组，这是一个深拷贝
"""
arr3 = arr2.astype(np.float64)

print(arr1)
print(arr2)
print(arr3)

"""
特殊形状数组：全0(zeros)，全1(ones),没有具体值的（未经过初始化的垃圾值）数组(empty)
"""
arr_0 = np.zeros(6)
arr_1 = np.ones((2,5))
arr_e = np.empty((2,3,5))
print(arr_0)
print(arr_1)
print(arr_e)

"""
arange指定范围
"""

arr4 = np.arange(4)
arr5 = np.arange(0,13,2,dtype = float)

print(arr4)
print(arr5)

"""
生成网格数据：指定起始点，终止点，以及网格点的个数
"""

arr6 = np.linspace(0,100,5)
print(arr6)

"""
简单运算
"""
#生成一个6x4的二维数组
a = np.arange(24).reshape((6,4))
#然后将其展平，即将其转化为一个24项的一维数组
b = a.flatten()
#将6x4的二维数组转化为3x8的二维数组
c = a.resize((3,8))
#矩阵的转置
d = a.transpose()