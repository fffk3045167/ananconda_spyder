# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 15:51:39 2019

@author: Administrator
"""

"""
Series数据对象使用方法
构成Pandas的三大数据结构基石是：Series、DataFrame、Index。
Series对象是一个带索引数据的一维数组，可以视作是增强版的NumPy结构。
"""

import pandas as pd

ser_data = pd.Series([0.25,0.5,0.75,4])

print(ser_data)

print(ser_data.values)
print(type(ser_data.values))
print(ser_data.index)
print(type(ser_data.index))

"""
Series可以显式定义索引，且可以是任意类型：整数（任意顺序）、字符串、日期类型等等
而一维数组Numpy数组则是隐式定义的整数索引
"""
ser_index = pd.Series([0.25,0.5,0.75,4], index = ['aa','bb','cc','dd'])

print(ser_index['cc'])

"""
分片操作，两端都包含
"""

print(ser_index['bb': 'dd'])
print(type(ser_index['bb': 'dd']))

"""
可用字典生成Series，同时可增加索引参数index进行筛选
"""

a_dict = {'one': 123,'acc': 120,'dir': 333}

ser_dict1 = pd.Series(a_dict,index = ['one','acc'])
ser_dict2 = pd.Series(a_dict,index = ['one','acc','none'])

print(ser_dict1)
print(ser_dict2)

