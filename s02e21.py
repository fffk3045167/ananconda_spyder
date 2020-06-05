# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 13:05:43 2019

@author: Administrator
"""

"""
matplotlib数据可视化之坐标轴与主次刻度用法详解
"""

import numpy as np
import matplotlib.pyplot as plt

"""
plt和坐标轴对象ax的关系

"""

"""
使用plt绘制
"""
x = np.linspace(0, 10, 100)
plt.subplot(2, 1, 1)
#绘制第一个子图
plt.plot(x, np.sin(x))

plt.subplot(2, 1, 2)
#绘制第二个子图
plt.plot(x, np.cos(x))

plt.show()

"""
使用坐标对象ax
"""

fig, ax = plt.subplots(2, 1)
#用对应的坐标轴对象绘制子图
ax[0].plot(x, np.sin(x))
ax[1].plot(x, np.cos(x))
plt.show()

"""
主刻度与次刻度
"""
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

fig = plt.figure()

xmajorLocator = MultipleLocator(20)  #将x轴主刻度标签设置为20的倍数
xmajorFormatter = FormatStrFormatter('%1.1f')  #设置x轴标签的文本格式
xminorLocator = MultipleLocator(5)  #将x轴次刻度标签设置为5的倍数

ymajorLocator = MultipleLocator(0.5)  #将y轴主刻度标签设置为0.5的倍数
ymajorFormatter = FormatStrFormatter('%1.1f')  #设置y轴标签的文本格式
yminorLocator = MultipleLocator(0.1)  #将y轴次刻度标签设置为0.1的倍数

ax = plt.subplot(111)
ax.xaxis.set_major_locator(xmajorLocator)
ax.xaxis.set_major_formatter(xmajorFormatter)

ax.yaxis.set_major_locator(ymajorLocator)
ax.yaxis.set_major_formatter(ymajorFormatter)

#显示次刻度标签的位置，无文本
ax.xaxis.set_minor_locator(xminorLocator)
ax.yaxis.set_minor_locator(yminorLocator)

ax.xaxis.grid(True, which = 'major')  #x轴网格使用主刻度
ax.yaxis.grid(True, which = 'minor')  #y轴网格使用次刻度

t = np.arange(100)
s = np.sin(0.1*np.pi*t)*np.exp(-t*0.01)
plt.plot(t, s, '--r*')
plt.show()

"""
格式生成器与定位器
先分别生成X轴的主定位器、主格式生成器，
再生成X轴的次定位器（由于X轴次要坐标没有刻度值，所以省去了次要格式生成器）
然后再利用坐标轴ax的xaxis.set_major_locator、
xaxis.set_major_formatter和xaxis.set_minor_locator方法，
分别对定位器和格式生成器进行赋值
即：通过定义每个坐标轴的locator和formatter对象，来完成刻线位置和标签等属性的设置
"""

"""
字符串前边的r代表是原始字符串，表示里边的内容不需要转义，一般出现在正则表达式，
这里是laText的用法，在python中使用laText，需要在文本的前后加上$符号，
剩下就是laText文本，matplotlib会自动解析，这里\pi代表的就是π。
"""

def format_func(value, tick_number):
    N = int(np.round(2 * value / np.pi))
    if N == 0:
        return '0'
    elif N  == 1:
        return r'$\pi/2$'
    elif N == 2:
        return r'$\pi$'
    elif N % 2 > 0:
        return r'${}\pi/2$'.format(N)
    else:
        return r'${}\pi$'.format(N / 2)


x = np.linspace(0, 3 * np.pi, 100)
plt.plot(x, np.sin(x))
ax = plt.axes()
ax.xaxis.set_major_locator(plt.MultipleLocator(np.pi / 2))
ax.xaxis.set_minor_locator(plt.MultipleLocator(np.pi / 4))
ax.xaxis.set_major_formatter(plt.FuncFormatter(format_func))
ax.grid(True)
plt.show()