# -*- coding: utf-8 -*-
"""
Created on Mon May 27 21:43:05 2019

@author: 鱼红叶

给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，
返回移除后数组的新长度。
"""

class Solution:
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1
        