# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 16:39:41 2019

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt

"""
绘制这样一组散点图，
每个点的位置坐标（x,y）是服从标准正态分布的随机值，
点的颜色灰度值是位于（0,1）空间中的随机样本，点的大小是随机值得1000倍，单位是像素。
"""
rng = np.random.RandomState(6)

x = rng.randn(100)
y = rng.randn(100)
colors = rng.rand(100)
sizes = 1000 * rng.rand(100)
plt.scatter(x,y,c = colors,s = sizes,alpha = 0.3)
plt.colorbar()
plt.grid()
plt.show()

"""
通过指定hist函数中的一些参数，来个性化的调整频次直方图的显示效果
bins参数可以指定数据条的个数
normed可以指定是否将频数进行标准化
alpha指定透明度,还有histtype、color、edgecolor等线性、颜色等参数
"""

data = np.random.randn(1000)
ret = plt.hist(data)
print(ret)
plt.show()

plt.hist(data, bins = 40, normed = True, alpha = 0.5,
         histtype = 'stepfilled', color = 'steelblue')
plt.grid(True)
plt.show()

data1 = np.random.normal(0,0.8,1000)
data2 = np.random.normal(-2,1,1000)
data3 = np.random.normal(3,2,1000)
plt.grid(True)
kwargs = dict(histtype = 'stepfilled', alpha = 0.5, density = True, bins = 40)
plt.hist(data1, **kwargs)
plt.hist(data2, **kwargs)
plt.hist(data3, **kwargs)
plt.show()
