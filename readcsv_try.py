# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 13:11:26 2019

@author: Administrator
"""

import numpy as np

#d = a.transpose()
"""
csv数据的读取
np.loadtxt(fname, dtype=, comments='#', delimiter=None, converters=None, skiprows=0, usecols=None, unpack=False, ndmin=0)
fname:文件名
dtype:指定类型,默认双精度浮点数
comments = '#':跳过开头为#的行
delimiter = ',':分隔符
converters = {0:add_one}:converters是一个字典参数,对数据进行预处理。表示第零列使用函数add_one来进行预处理
skiprows = 1:跳过前1行
usecols = (0,2):只使用第0、2行
unpack = True:是指会把每一列当成一个向量输出, 而不是合并在一起
ndmin:指定数组的维数
"""
c,v = np.loadtxt('datefile.csv',delimiter = ',',usecols = (1,2), unpack = True)

print(c)
print(type(c[1]))
print(v)

#算术平均

mean_c = np.mean(c)
print(mean_c)

#加权平均

vwap = np.average(c, weights = v)
print(vwap)

#最值
print(np.min(c))
print(np.max(c))
print(np.ptp(c))  #最值之差
print(np.median(c))  #中位数
"""
方差:方差指的是各个数据与所有数据算数平均数的离差平方和的均值
"""
print(np.var(c))  #或
print(np.mean((c - c.mean()) ** 2))

"""
常用指标分析方法
收益率分析
波动率计算
日期处理方法
"""
"""
收益率分析:用今天的收盘价减去昨天的收盘价，再除以昨天的收盘价格。
"""
returns = -np.diff(c) / c[1:]
print(returns)
print(np.std(returns))  #标准差
print(np.where(returns > 0))

"""
波动率计算：使用对数收益率
专业上我们对价格变动可以用一个叫做“波动率”的指标进行度量。
计算历史波动率时需要用到对数收益率，对数收益率很简单，
就是logC(t+1)/C(t),等于logC(t+1)−logC(t)
计算年化波动率时，要用样本中所有的对数收益率的标准差除以其均值，再除以交易日倒数的平方根，一年交易日取252天。
"""

logreturns = -np.diff(np.log(c))
volatility = np.std(logreturns) / np.mean(logreturns)
annual_volatility = volatility / np.sqrt(1. / 252.)
print(volatility)
print(annual_volatility)