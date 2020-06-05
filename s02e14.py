# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 14:38:12 2019

@author: Administrator
"""

"""
DataFrame数据连接的三种关系代数
一对一连接、多对一连接、多对多连接
"""
#import numpy as np
import pandas as pd

df1 = pd.DataFrame({'employee': ['Bob', 'Jake', 'Lisa', 'Sue'],
                    'group': ['MGR', 'R&D', 'HR', 'R&D']})
df2 = pd.DataFrame({'employee': ['Bob', 'Jake', 'Sue', 'Lisa'],
                    'hire_date': [2004, 2009, 2013, 2010]})

print(df1)
print(df2)

"""
一对一连接是最简单的数据合并类型，
他指的是两个待连接的DataFrame数据对象有一个完全相同的属性列，
并自动以这一列作为键进行连接，生成一个新的DataFrame数据对象，
这样就能合并之前数据里的其他不同属性，通过merge方法即可实现
"""
df3 = pd.merge(df1,df2)
print(df3)

