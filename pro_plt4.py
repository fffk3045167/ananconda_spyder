# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 15:35:40 2019

@author: Administrator
"""

"""
饼图
"""
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['KaiTi']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

plt.figure()
dataList = [10, 12, 15, 18, 9, 25]
dataLabel = ["水", "零食", "水果", "生活用品", "外卖", "电影"]

plt.pie(dataList, labels=dataLabel, colors=["r", "y", "g", "b", "c", "m"], autopct="%1.2f%%")
# 显示图例
plt.legend()

plt.title("一天的消费情况")
# 将当前的图形变成圆形，默认为椭圆
plt.axis("equal")

plt.show()
