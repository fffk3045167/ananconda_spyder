# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 16:58:31 2019

@author: Administrator
"""

"""
服从参数为(n,p)的二项分布的随机变量X,他的期望和方差为
期望: E[X] = np
方差: V[X] = np(1-p)
"""

import numpy as np
from scipy.stats import binom

#用函数包中的方法计算的分布的理论值
binom_rv = binom(n = 10, p = 0.5)
mean, var, skew, kurt = binom_rv.stats(moments = 'mvsk')

#从模拟试验得到的数据中计算出来的均值和方差
binom_rvs = binom_rv.rvs(size = 100000)
E_sim = np.mean(binom_rvs)  #期望
S_sim = np.std(binom_rvs)  #标准差
V_sim = S_sim * S_sim  #方差

print('mean = {}, var = {}'.format(mean,var))
print('E_sim = {}, V_sim = {}'.format(E_sim,V_sim))
#通过公式直接计算出来的理论值
print('E = np = {}, V = np(1-p) = {}'.format(10 * 0.25,10 * 0.25 * 0.75))
