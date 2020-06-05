# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 13:16:49 2020

@author: Administrator
"""

"""
给定一个包含红色、白色和蓝色，一共n个元素的数组，原地对它们进行排序，
使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

"""

nums = [2,0,2,1,1,0]
p = 0
p_left = 0
p_right = len(nums) - 1

while p <= p_right:
    if nums[p] == 0:
        nums[p], nums[p_left] = nums[p_left], nums[p]
        p_left += 1
        p += 1
    elif nums[p] == 2:
        nums[p], nums[p_right] = nums[p_right], nums[p]
        p_right -= 1
    else:
        p += 1

print(nums)