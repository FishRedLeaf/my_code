# -*- coding: utf-8 -*-
"""
Created on Tue May 28 21:46:49 2019

@author: 鱼红叶

给定一个整数数组 nums 和一个目标值 target，
请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        
        维护一个hash表，边遍历数组边存储值到hash表中，
        当遍历到nums[i]时，如果hash[target - nums[i]] > 0，那么就找到了符合条件的两个值
        """
        
        d = {}
        res = []
        for i, n in enumerate(nums):
            if target-n in d:
                res.append(d[target-n], i)
            d[n] = i
        return res
        