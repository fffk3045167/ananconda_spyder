# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 15:44:01 2019

@author: Administrator
"""

"""
散点图、
"""

import matplotlib.pyplot as plt
import random

plt.rcParams['font.sans-serif'] = ['KaiTi']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False

plt.figure()
month_days = 31

x = [i for i in range(1, month_days)]
y = [random.randrange(20, 40) for i in range(1, month_days)]

plt.scatter(x, y)

plt.xlabel("一个月")
plt.ylabel("消费金额")
plt.title("一个月的中餐的消费情况")
plt.show()