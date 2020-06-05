# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 14:00:23 2019

@author: Administrator
"""

import numpy as np
import pandas as pd


"""
缺失值的表征方式
python中采用一种NaN（Not a Number）标签来表示缺失值，NaN本质上是一种浮点数类型
"""
var = np.array([1,np.nan,2,3])
print(var)
print(var.dtype)

"""
缺失值的运算处理规则,任何数与之运算，其结果都是NaN
"""

print(np.nan + 1)
print(np.nan * 3)
print(var.sum())
print(var.max())

"""
在NumPy中忽略掉NaN缺失值进行一些运算
"""
print(np.nansum(var))
print(np.nanmax(var))

"""
浮点类型缺失值的例子，将整数型Series中的某值设置为缺失型，整个Series将强制变成浮点型
"""

ser = pd.Series([1,2],dtype = int)

print(ser)
ser[0] = np.nan
print(ser)

"""
如果Series中的数据类型是字符串，由于字符串是object类型，
因此将该类型的Series中的某个字符串数据设置为缺失型，整个类型仍是object类型
"""

obj = pd.Series(['a','b'])

print(obj)
obj[0] = np.nan
print(obj)

"""
用isnull()和notnull()两种方法来发现缺失值
"""

ser_nan = pd.Series([1,np.nan,3,np.nan,'eq'])

print(ser_nan.isnull())
print(ser_nan.notnull())

"""
两种方法，返回的都是布尔型的掩码数据，
isnull()会在为空的位置上显示True，notnull则正好相反
布尔型掩码数据可以作为一种过滤工具
"""

print(ser_nan[ser_nan.notnull()])

"""
丢弃缺失值
Series数据类型对于缺失值的处理很简单，就是简单的丢弃相应的值
DataFrame就要复杂一些，他无法简单的单独剔除掉一个缺失值，要么剔除缺失值所在的整行，
要么剔除掉整列，默认是剔除行，如果要剔除所在列的话，需要单独设置axis=1的关键字参数
"""
#Series丢弃缺失值
print(ser_nan.dropna())
#DataFrame丢弃缺失值
df = pd.DataFrame([[1,np.nan,2],[2,3,5],[np.nan,4,6],[np.nan,np.nan,np.nan]])

print(df)
#默认丢弃缺失值所在行
print(df.dropna())
#设置axis=1的关键字参数，丢弃缺失值所在列
print(df.dropna(axis = 1))
"""
在dropna（）函数中还有一个非常重要的参数how，
默认how=any，表示此行（或列）只要有一个NaN值，就要删除所在行（或列）
当how=all是表示只有当此行（或列）全部都是NaN值时，才执行此操作。
"""
print(df.dropna(how = 'any'))
print(df.dropna(how = 'all'))
print(df.dropna(how = 'all',axis = 1))

"""
DataFrame阈值控制丢弃
"""
