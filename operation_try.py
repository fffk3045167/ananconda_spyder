# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 10:27:18 2019

@author: Administrator
"""

import numpy as np
import pandas as pd

"""
Series与DataFrame对象的数值运算 
"""

"""
一元运算作用于每一个数据元素
"""
ser = pd.Series([2,4,6,8],index = ['a','b','c','d'])

print(ser)
print(np.exp(ser))

rng1 = np.random.RandomState(18)
df = pd.DataFrame(rng1.randint(0,10,(3,4)),columns = ['a','b','c','d'])

print(df)
print(np.sin(df * np.pi / 4))

"""
二元运算
"""

ser1 = pd.Series({'a': 10,'b': 20,'d': 40})
ser2 = pd.Series({'b': 2,'c': 4,'d': 4})
print(ser1 /ser2)

"""
缺失值的处理：设置参与运算的Series，其索引缺失位置的数据为0
"""
print(ser1.add(ser2,fill_value = 0))

rng2 = np.random.RandomState(10)
data1 = pd.DataFrame(rng2.randint(0,20,(2,2)),columns = ['A','B'])
data2 = pd.DataFrame(rng2.randint(0,10,(3,3)),columns = ['B','C','A'])

print(data1)
print(data2)
"""
+，-，*，/这些属于python运算符，如果我们需要加上一些控制用的关键字，
如：填充缺失值fill_value，就需要使用Pandas的对应方法add()，sub()，mul()，div()
"""
print(data1 + data2)
print(data1.add(data2,fill_value = data1.stack().mean()))

"""
行维度上的计算
DataFrame的每一行都减去由自己第一行数据构成的Series对象
通过索引器iloc得到第一行数据（Series类型），然后用DataFrame每行数据减去第一行数据
"""
rng3 = np.random.RandomState(33)
data3 = pd.DataFrame(rng3.randint(0,10,(3,4)),columns = ['A','B','C','D'])
print(data3)
print(data3 - data3.iloc[0])

"""
列维度上的计算 DataFrame - Series
    
"""

print(data3.sub(data3['B'], axis = 0))
"""
DataFrame与Series的运算同样也是要对齐指定方向上的索引，
索引不一致处的运算，也会用NaN进行空值处理
"""