# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 19:14:32 2019

@author: Administrator
"""
"""
一个数如果恰好等于它的因子之和，这个数就称为“完数”。
例如6=1＋2＋3.找出1000以内的所有完数
"""

def perfect_num(n):
    array = []
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            array.append(i)
#    print(array)
    for i in range(len(array)):
            sum = sum + array[i]
    if sum == n:
        print('perfect number: {}'.format(n))
    return n


if __name__ == '__main__':
    a = 2
    b = 10000
    for i in range(a, b + 1):
        perfect_num(i)