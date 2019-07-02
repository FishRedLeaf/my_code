# -*- coding: utf-8 -*-
"""
Created on Tue May 28 21:50:57 2019

@author: 鱼红叶
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        d = {}
        for i, n in enumerate(nums):
            d[n] = d.get(n, 0) + 1
        for k, v in d.items():
            if v > len(nums) // 2:
                return k