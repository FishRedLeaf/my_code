# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 19:53:55 2019

@author: 鱼红叶
"""

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        
        1. 从后往前遍历数组，找到数值开始减小的那个位置idx，即nums[idx-1] < nums[idx]；
        2. 令idx_l = idx-1，从idx位置从前往后移动直到找到最后一个数值大于nums[idx_l]的元素；
        3. 交换nums[idx_l]和nums[idx]的值；
        4. 反转数组在idx位置之后的所有元素。
        
        e.g. 
        1 2 7 4 3 1
        idx = index of 2
        """
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                idx_l = i-1
                break
        idx = idx_l+1
        for i in range(idx_l+1, len(nums)):
            if nums[i] < nums[idx] and nums[i] > nums[idx_l]:
                idx = i
        nums[idx_l], nums[idx] = nums[idx], nums[idx_l]
        nums[idx_l+1:] = nums[idx_l+1:][::-1]
        
    def nextPermutation2(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return 
        
        idx = 0
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                idx = i
                break
        
        if idx != 0:
            for i in range(len(nums)-1, idx-1, -1):
                if nums[i] > nums[idx-1]:
                    nums[i], nums[idx-1] = nums[idx-1], nums[i]
                    break
        nums[idx:] = nums[idx:][::-1]

nums = [1,2,7,4,3,1]
Solution().nextPermutation(nums)
print(nums)












