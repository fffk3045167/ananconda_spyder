# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 10:59:54 2020

@author: Administrator
"""

nums = [0,1,2,2,3,0,4,2]
val = 2

for i in range(len(nums)):
    if nums[i] == val:
        nums.pop(i)
print(len(nums))
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = len(nums)
        i = 0
        j = 0
        while j < length:
            if nums[j] != val:
                nums[i] = nums[j]
                i = i + 1
                j = j + 1
            else:
                j = j + 1
        res = length - (j - i)
        return res


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)):
            if nums[i] == val:
                nums.pop(i)
        return len(nums)


def removeElement(nums, val):
    # i为不同元素的数组的长度
    i = 0
    for j in range(0, len(nums)):
        # 如果nums[j]不等于val, 则将nums[j]赋值给nums[i]即可, i自增
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    return i

print(removeElement([3,2,2,3], 3))
print(removeElement([0,1,2,2,3,0,4,2], 2))
