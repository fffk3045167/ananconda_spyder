# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 19:41:36 2019

@author: Administrator
"""

"""
避免一次性生成整个结果列表的本质是在需要的时候才逐次产生结果，而不是立即产生全部的结果
"""
"""
def gen_squares(num):
    for x in range(num):
        yield x ** 2

gen1 = gen_squares(4)

print(gen1)
"""
"""
生成器函数
"""
def gen_squares(num):
    for x in range(num):
        yield x ** 2
        print('x={}'.format(x))

for i in gen_squares(4):
    print('x ** 2={}'.format(i))
    print('--------------')
    
"""
生成器
"""
print([x ** 2 for x in range(5)])   #列表解析式
print((x ** 2 for x in range(5)))  #生成器表达式
