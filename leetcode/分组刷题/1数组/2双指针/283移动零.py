# -*- coding: utf-8 -*-
"""
Created on Sat May 25 18:26:48 2019

@author: Administrator
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
        nums[i:] = [0] * (len(nums[i:]))

nums = [1,0,2,0,5]
Solution().moveZeroes(nums)
print(nums)
        