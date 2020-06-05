# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 15:56:16 2019

@author: Administrator
"""

"""
三维图
最基本的三维图是由(x, y, z)三维坐标点构成的线图与散点图，
可以用ax.plot3D和ax.scatter3D函数来创建，
默认情况下，散点会自动改变透明度，以在平面上呈现出立体感
"""

from mpl_toolkits import mplot3d
#matplotlib inline
import matplotlib.pyplot as plt
import numpy as np

ax = plt.axes(projection='3d')

#三维线的数据
zline = np.linspace(0, 15, 1000)
xline = np.sin(zline)
yline = np.cos(zline)
ax.plot3D(xline, yline, zline, 'gray')

# 三维散点的数据
zdata = 15 * np.random.random(100)
xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
ydata = np.cos(zdata) + 0.1 * np.random.randn(100)
ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens')
