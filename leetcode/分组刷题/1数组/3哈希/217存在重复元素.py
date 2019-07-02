# -*- coding: utf-8 -*-
"""
Created on Tue May 28 21:44:16 2019

@author: 鱼红叶
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        
        利用unordered_set无序集合，遍历数组的时候将元素放入集合中，
        找出已经在集合中出现的元素就是重复的元素
        """
        
        d = {}
        for i, n in enumerate(nums):
            d[n] = d.get(n, 0) + 1
            if d[n] > 1:
                return True
        return False
        