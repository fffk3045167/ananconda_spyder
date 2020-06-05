# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 09:39:42 2019

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10)
plt.axes([0.1, 0.5, 0.8, 0.4], ylim = (-1.2, 1.2))
plt.grid(True)
plt.plot(np.sin(x))

plt.axes([0.1, 0.1, 0.8, 0.4], ylim = (-1.2, 1.2))
plt.grid(True)
plt.plot(np.cos(x))
plt.show()

"""
subplot方法无法绘制比例自定义的子图，而是只能创建彼此对齐的行列网格子图
plt.subplots_adjust方法，
设置子图之间的纵、横两方向上的间隙，子图中的文本就是他的编号规则
"""
plt.subplots_adjust(hspace = 0.3, wspace = 0.3)
for i in range(1,7):
    plt.subplot(2, 3, i)
    plt.text(0.5, 0.5, str((2,3,i)), fontsize = 18, ha = 'center')

plt.show()

"""
子图之间共用坐标轴的用法
"""
fig, ax = plt.subplots(2, 3, sharex = 'col', sharey = 'row')
print(ax)
plt.show()

"""
GridSpec绘制不规则多行多列子图的方法
得到一个长×宽为2×3的grid区域，这个grid的原点是左上角，
第一行第一列的子图占据grid的第0个长度，第0个宽度；
第一行第二列子图占据grid的第0个长度，第1和第2个宽度（因此用分片1:3来表示）
其他的以此类推
"""

grid = plt.GridSpec(2, 3, wspace = 0.5, hspace = 0.5)
plt.subplot(grid[0,0])
plt.subplot(grid[0,1:3])
plt.subplot(grid[1,0:2])
plt.subplot(grid[1,2])
plt.show()
