# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 14:51:08 2019

@author: Administrator
"""

"""
某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，加密规则如下：
每位数字都加上5,然后用和除以10的余数代替该数字，
再将第一位和第四位交换，第二位和第三位交换。
"""

#输入数据
def inputnum(numbers):
    numbers = int(input('请输入四位数的整数: '))
    return numbers

#加密
def encryption(data):
    array = []
    array.append(data // 1000)
    array.append(data % 1000 // 100)
    array.append(data % 100 // 10)
    array.append(data % 10)
    for i in range(len(array)):
        array[i] += 5
        array[i] %= 10
    array[0], array[2] = array[2], array[0]
    array[1], array[3] = array[3], array[1]
    for i in range(len(array)):
        print(array[i], end = '')
    return data

if __name__ == '__main__':
    data = int(input('请输入四位数的整数: '))
    print('加密后数据为:', end = ' ')
    encryption(data)