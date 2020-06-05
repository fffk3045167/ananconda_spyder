# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 13:32:46 2019

@author: Administrator
"""

"""
python 求逆矩阵
"""

import numpy as np
from scipy import linalg

A = np.array([[1, 35, 0],
              [0, 2, 3],
              [0, 0, 4]])

print(A)
#逆矩阵
A_n = linalg.inv(A)
print('原矩阵：\n{}'.format(A))
print('逆矩阵：\n{}'.format(A_n))
#原矩阵和逆矩阵相乘，可以得到单位矩阵
print('单位矩阵：\n{}'.format(np.dot(A, A_n)))

"""
求矩阵的秩
"""

B = np.array([[1, 0, 0],
              [0, 2, 0],
              [0, 0, 4]])
C = np.array([[1, 0, 2],
              [0, 1, 3],
              [1, 1, 5]])
D = np.array([[1, 2, 3],
              [2, 4, 6],
              [3, 6, 9]])

print(np.linalg.matrix_rank(B))
print(np.linalg.matrix_rank(C))
print(np.linalg.matrix_rank(D))