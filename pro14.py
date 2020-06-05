# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 15:48:14 2019

@author: Administrator
"""
"""
import time
print('下载中',end = '')
for i in range(5):
    print('.',end = '')
    time.sleep(1)
print('\n下载完成！')
"""
"""
将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

程序分析：对n进行分解质因数，应先找到一个最小的质数k，然后按下述步骤完成： 
(1)如果这个质数恰等于n，则说明分解质因数的过程已经结束，打印出即可。
(2)如果n>k，但n能被k整除，则应打印出k的值，并用n除以k的商,作为新的正整数你n,
　重复执行第一步。
(3)如果n不能被k整除，则用k+1作为k的值,重复执行第一步。
"""


def output(number,array):
    print('因式分解为: {} = '.format(number), end = '')
    for i in range(len(array)):
        if i < len(array) - 1:
            print('{}*'.format(array[i]), end = '')
    print(array[len(array) - 1])


def Factorization(n):
    array = []
    num = n
    for i in range(2, n + 1):
        while n != i:
            if n % i == 0:
                array.append(i)
                n = n // i
            else:
                break
        if n == i:
            array.append(i)
    output(num,array)


if __name__ == '__main__':
    number = int(input('输入一个大于1正整数: '))
    Factorization(number)
