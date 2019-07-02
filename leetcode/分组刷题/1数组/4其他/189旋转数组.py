# -*- coding: utf-8 -*-
"""
Created on Wed May 29 22:17:48 2019

@author: 鱼红叶
"""

class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        # l = len(nums)
        # nums[:] = nums[l-k:] + nums[:l-k]
        
        # nums1 = nums[:]
        # l = len(nums)
        # for i in range(l):
        #     nums[(i+k)%l] = nums1[i]
        
        l = len(nums)
        nums[l-k:] = nums[l-k:][::-1]
        nums[:l-k] = nums[:l-k][::-1]
        nums[:] = nums[::-1]