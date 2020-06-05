# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 11:14:12 2019

@author: Administrator
"""
import numpy as np
import matplotlib.pyplot as plt

mean = [0, 0]
cov = [[1, 1], [1, 4]]
x, y = np.random.multivariate_normal(mean, cov, 3000).T
plt.figure(figsize = (6, 6))
grid = plt.GridSpec(4, 4, wspace = 0.5, hspace = 0.5)

main_ax = plt.subplot(grid[0:3, 1:4])
plt.plot(x, y, 'ok', markersize = 3, alpha = 0.2)

#和大子图共Y轴
y_hist = plt.subplot(grid[0:3, 0], xticklabels = [], sharey = main_ax)
#图形水平绘制
plt.hist(y, 60, orientation = 'horizontal', color = 'gray')
#x轴调换方向
y_hist.invert_xaxis()

#和大子图共x轴
x_hist = plt.subplot(grid[3,1:4],yticklabels=[],sharex=main_ax)
#图形垂直绘制
plt.hist(x,60,orientation='vertical', color='gray')
#y轴调换方向
x_hist.invert_yaxis()

plt.show()