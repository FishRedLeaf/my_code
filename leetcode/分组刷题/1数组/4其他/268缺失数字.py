# -*- coding: utf-8 -*-
"""
Created on Wed May 29 22:16:17 2019

@author: 鱼红叶
"""

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(len(nums)+1):
            ans ^= i
        for n in nums:
            ans ^= n
        return ans