# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 14:52:45 2019

@author: Administrator
"""

import pandas as pd

area = pd.Series({'California':423967,'Texas':695662,
                  'New York':141297,'Floriade':170312,
                  'Illinois':149995})

pop = pd.Series({'California':38332521,'Texas':26448193,
                 'New York':19651127,'Floriade':19552860,
                 'Illinois':12882135})

data = pd.DataFrame({'list1': area,'list2': pop})

print(data)
#取相应的列
print(data['list2'])

"""
使用字典进行语法扩充

"""
data['a'] = [1,2,3,4,None]  #添加新列a，并赋值一个向量数组
data['b'] = 3          #添加新列b，并赋值一个标量

data['density'] = data['list2'] / data['list1']   #两列之间的运算

print(data)

"""
三种索引器的行列索引方法
1、iloc索引，采用隐式的整数索引进行分片，规则都是左闭右开
2、loc索引，则是采用显式的标签值索引进行分片，规则是左右都取
3、ix索引，用隐式整数索引进行行的分片，利用显式标签名称进行列的分片
"""

print(data.iloc[:2,1:2])

print(data.loc[:'Texas','list1':'list2'])

print(data.ix[:3,'list1':'list2'])

print(data.ix[:3,['list1','a']])    #选取非连续的列

"""
DataFrame的条件过滤操作
"""

print(data.loc[data['density'] > 0],['area','density'])

"""
DataFrame数据值的修改
"""

data.loc['Floriade','area'] = 66666
data.iloc[4,2] = 32 