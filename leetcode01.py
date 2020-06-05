# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 09:11:16 2020

@author: Administrator
"""

"""
给定一个整数数组和一个目标值，找出数组中和为目标值的 两个数。
你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。
示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""

nums = [2, 7, 11, 16, 15]
target = 18

"""
for i in range(len(nums)):
    for j in range(1, len(nums)):
        if nums[i] + nums[j] == target:
            print([i, j])
            break
"""
for i in range(len(nums)):
    if target - nums[i] in nums:
        print([i, nums.index(target - nums[i])])
        break