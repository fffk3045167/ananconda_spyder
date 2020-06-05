# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 15:00:40 2019

@author: Administrator
"""

"""
多级索引的Series类型

"""

import numpy as np
import pandas as pd

index1 = [('California', 2008), ('California', 2018),
         ('New York', 2008), ('New York', 2018),
         ('Texas', 2008), ('Texas', 2018)]

mul_index = pd.MultiIndex.from_tuples(index1)

print(mul_index)
population = [33870000, 37250000,
              18970000, 19370000,
              20850000, 25140000]
pop = pd.Series(population, index = mul_index)
print(pop)

#获取2018年的数据
print(pop[:, 2018])

"""
unstack( )方法可以使一个带有多级索引的Series转化为一个普通的DataFrame对象
stack( )方法实现的则是相反方向的操作
"""
df_pop = pop.unstack()
print(df_pop)
print(df_pop.stack())

"""
多级索引DataFrame类型

"""
under_18_pop = [9267089, 9284094, 4687374, 4318033, 5906301, 6879014]
pop_df = pd.DataFrame({'total': pop,'under18': under_18_pop})
print(pop_df)

"""
多级索引的创建方法
1、嵌套列表创建
2、levels和labels标签直接创建
3、索引"相乘"形式创建
"""

mul_index_list = pd.MultiIndex.from_arrays([['a', 'a', 'b', 'b'],[1,2,1,2]])
print(mul_index_list)


mul_index_levels = pd.MultiIndex(levels = [['a','b'],[0,1]],
                                 labels = [[0,0,1,1],[1,0,1,0]])
print(mul_index_levels)

mul_index_multiply = pd.MultiIndex.from_product([[2008,2018],[1,2]])
print(mul_index_multiply)

#给每一个索引都加一个名字
pop.index.names = ['state','year']
print(pop)

"""
多级行索引和多级列索引举例
"""

index_test = pd.MultiIndex.from_product([[2008,2018],[1,2]],
                                        names = ['year','visit'])
coloums_test = pd.MultiIndex.from_product([['Tom','Bill'],[22,18]],
                                          names = ['name','age'])

data = np.random.randn(4,4)
df_data = pd.DataFrame(data, index = index_test, columns = coloums_test)
print(df_data)