# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 15:04:01 2019

@author: Administrator
"""

import seaborn as sns
import numpy as np
import pandas as pd

planets = sns.load_dataset('planets')

print(planets.head())

print(planets.groupby('method')['distance'].mean())

"""
累计

"""
rng = np.random.RandomState(0)
df = pd.DataFrame({'key': ['A','B','C','A','B','C'],
                   'data1': range(6),
                   'data2': rng.randint(0,10,6)})
print(df)
"""
以key作为分组，对每一组分别求最大值、最小值和中位数，
"""
print(df.groupby('key').aggregate(['min',np.median,'max']))
"""
或者针对每个不同的属性列使用各自不同的累计方法
"""
print(df.groupby('key').aggregate({'data1': 'min','data2': 'max'}))

"""
转换
返回的是一个全量数据，其形状与原始输入数据一致
"""

print(df.groupby('key').transform(lambda x: x - x.mean()))