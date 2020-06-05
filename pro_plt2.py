# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 14:38:27 2019

@author: Administrator
"""

"""
直线、中文显示
"""

import numpy as np
import matplotlib.pyplot as plt

#用来正常显示中文
plt.rcParams['font.sans-serif'] = ['KaiTi']
#用来正常显示负号
plt.rcParams['axes.unicode_minus'] = False

plt.figure()

fig, (axes1, axes2) = plt.subplots(nrows = 1, ncols = 2)

'''
第一个子图
'''
axes1.plot(np.arange(5), color = 'r', linestyle = '-.', label = 'red line')
#设置当前标题
axes1.set_title('图1')
#设置当前x轴和y轴的标签
axes1.set_xlabel(xlabel = 'x轴')
axes1.set_ylabel(ylabel = 'y轴')
#显示图例
axes1.legend()

#设置网格
axes1.grid(True, linestyle = '-.', alpha = 0.5)

'''
第二个子图
'''
axes2.plot([2,4,6,8], color = 'y', linestyle = '--', label = 'yellow line')
axes2.set_title('图2')
#设置第二张图的刻度
axes2.set_xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
axes2.set_yticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
axes2.legend()

#开启刻度
axes2.minorticks_on()
plt.show()