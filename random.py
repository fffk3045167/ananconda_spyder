# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 13:26:52 2019

@author: Administrator
"""
import random
import numpy as np

"""
random模块
"""
#随机生成一个 [0,1) 的浮点数 
num1 = random.random()
print(num1)
#随机生成一个 [a,b) 的浮点数 
num2 = random.uniform(2,4)
print(num2)
#随机生成一个 [a,b] 的整数
num3 = random.randint(3,6)
print(num3)
#从一个已有的sequence中随机选择一个元素 
num4 = random.choice(range(2,10))
print(num4)
str1 = random.choice('ggrtxdsrreed')
print(str1)
#打乱一个列表的元素顺序 
list1 = ['香蕉','苹果','橘子','眼影','眼线']
random.shuffle(list1)
print(list1)

"""
numpy中的random函数
"""
#生成a*b维的随机数，且该数服从标准正太分布
data1 = np.random.randn(3,4)
print(data1)
#生成一个以[low,high)范围,size为大小的随机整数矩阵 
data2 = np.random.randint(low = 2, high = 8, size = (4,6))
print(data2)

"""
为了使得具备随机性的代码最终的结果可复现,使用RandomState获得随机数生成器
其中的111为随机数种子，只要随机数种子seed相同，产生的随机数系列就相同
"""

rng = np.random.RandomState(111)
arr1 = []
for i in range(12):
    arr1.append(rng.randint(10,99))
print(arr1)