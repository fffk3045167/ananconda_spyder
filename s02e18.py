# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 14:55:36 2019

@author: Administrator
"""

"""
matplotlib数据可视化之线形图绘制 

"""

import numpy as np
import matplotlib.pyplot as plt

x =  np.linspace(0,10,100)
plt.plot(x, np.sin(x))
plt.title('a sine curve')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.show()

"""
绘制f = x^3 + 2x^2 + 3x +4 函数图像
"""
#生成指定的多项式
func = np.poly1d(np.array([1,2,3,4]).astype(float))
#获得自变量X的取值
x = np.linspace(-10,10,30)
#获得结果y的数组
y = func(x)
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y(x)')
plt.show()
