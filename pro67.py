# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 13:40:12 2019

@author: Administrator
"""

"""
输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组
"""

#输入数组
def inputArray(numbers):
    inArray = []
    print('输入数字: ')
    for i in range(numbers):
        inArray.append(int(input()))
    return inArray

#找出最大值并与第一个元素交换
def changeMax(array):
    maxIndex = 0
    maxValue = array[0]
    for i in range(len(array)):
        if array[i] > maxValue:
            maxValue = array[i]
            maxIndex = i
              
    #进行交换
    temp = array[0]
    array[0] = maxValue
    array[maxIndex] = temp
    return array

#找出最小值并与最后一个元素交换
def changeMin(array):
    minIndex = 0
    minValue = array[0]
    for i in range(len(array)):
        if array[i] < minValue:
            minValue = array[i]
            minIndex = i
    #交换
    temp = array[len(array) - 1]
    array[len(array) - 1] = minValue
    array[minIndex] = temp
    return array

if __name__ == '__main__':
    arr = inputArray(5)
    print('原数组：{}'.format(arr))
    print('最大的与第一个元素交换后: {}'.format(changeMax(arr)))
    print('最小的与最后一个元素交换后: {}'.format(changeMin(arr)))