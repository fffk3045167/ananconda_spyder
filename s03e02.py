# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 15:27:39 2019

@author: Administrator
"""

"""
向量运算与空间坐标变换 
"""
"""
向量与向量的乘法分为所谓的点乘（内积）和叉乘（外积）
内积计算时无论是行向量间的内积还是列向量间的内积，其运算结果都是一样的，
但是python内积运算函数中的参数要求必须是行向量
"""

import numpy as np

x1 = np.array([1,2,3])
y1 = np.array([3,4,2])
print('向量x1与向量y1的点乘（内积）：{}'.format(np.dot(x1, y1)))

"""
向量在二维平面中的外积
"""
x2 = np.array([2,3])
y2 = np.array([3,5])
print('向量在二维平面中的外积:{}'.format(np.cross(x2, y2)))

"""
向量在三维平面中的外积，这个向量也是有物理含义的，即两个向量所表示平面的法向量
"""
x3 = np.array([2,4,5])
y3 = np.array([1,3,6])
print('向量在三维平面中的外积: {}'.format(np.cross(x3, y3)))