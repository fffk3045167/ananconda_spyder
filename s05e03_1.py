# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 13:42:32 2019

@author: Administrator
"""

"""
二项分布及二项随机变量
"""

#通过指定不同的参数，绘制PMF图

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import binom

sns.set()

k = np.arange(0, 11)

fig, ax = plt.subplots(2, 1)
fig.suptitle('binomial distribution PMF')
#生成指定n,p参数的二项随机变量
binom_rv_0 = binom(n = 10, p = 0.5)
binom_rv_1 = binom(n = 10, p = 0.25)

#绘制第一个PMF图
ax[0].plot(k, binom_rv_0.pmf(k), 'bo', ms = 8)
ax[0].vlines(k, 0,binom_rv_0.pmf(k), colors = 'b', lw = 5, alpha = 0.5)
ax[0].set_title('n = 10, p = 0.5')

#绘制第二个PMF图
ax[1].plot(k, binom_rv_1.pmf(k), 'ro', ms = 8)
ax[1].vlines(k, 0, binom_rv_1.pmf(k), colors = 'r', lw = 5, alpha = 0.5)
ax[1].set_title('n = 10, p = 0.25')

plt.show()

"""
随机变量的模拟
使用binom模块中的rvs方法进行二项随机变量的模拟
"""
