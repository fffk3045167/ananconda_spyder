# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 14:54:37 2019

@author: Administrator
"""

"""
向量和矩阵的python描述 
"""
import numpy as np

#生成矩阵
A = np.array([[1,3,5],[3,2,4]])
print(A)
print(A.shape)

#行列相等为方阵，行列数为阶数，3行即为3阶方阵
B = np.array([[1, 2, 3], [4, 5, 6],[7, 8, 9]])

#矩阵的转置,即行列互换
print(A.T)

"""
简单生成向量
向量可以看作是特殊的矩阵。
行向量是1×m的矩阵，列向量是n×1的矩阵
"""

C = np.array([[1,2,3]])

#行向量
print('行向量: {}'.format(C))
#列向量
print('列向量: \n{}'.format(C.T))

#零矩阵：所有元素都是0
O = np.zeros([3,5])
print('零矩阵: \n{}'.format(O))

#单位矩阵：对角线的元素均为1，其余元素均为0
I = np.eye(4)
print('4阶单位矩阵：\n{}'.format(I))

#对角矩阵：非对角线上的元素均为0
D = np.diag([1,3,4])
print('对角矩阵： \n{}'.format(D))