# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 13:16:31 2019

@author: Administrator
"""

"""
快速排序算法
"""

import numpy as np

def quickSort(arr, left=None, right=None):
    left = 0 if not isinstance(left, (int, float)) else left
    right = len(arr) - 1 if not isinstance(right, (int, float)) else right
    if left < right:
        partitionIndex = partition(arr, left, right)
        quickSort(arr, left, partitionIndex - 1)
        quickSort(arr, partitionIndex + 1, right)
    return arr

def partition(arr, left, right):
    pivot = left
    index = pivot + 1
    i = index
    while  i <= right:
        if arr[i] < arr[pivot]:
            swap(arr, i, index)
            index += 1
        i += 1
    swap(arr, pivot, index - 1)
    return index - 1

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

"""
实例
"""

if __name__ == '__main__':
    arr = []
    rng = np.random.RandomState(7)
    for i in range(20):
        arr.append(rng.randint(10, 99))
    print('排序前: {}'.format(arr))
    quickSort(arr)
    print('排序后: {}'.format(arr))