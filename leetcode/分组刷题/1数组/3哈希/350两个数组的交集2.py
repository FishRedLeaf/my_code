# -*- coding: utf-8 -*-
"""
Created on Tue May 28 20:30:19 2019

@author: 鱼红叶
"""

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d = {}
        for i, n in enumerate(nums1):
            d[n] = d.get(n, 0) + 1
            
        res = []
        for i, n in enumerate(nums2):
            if n in d:
                res.append(n)
                d[n] -= 1
                if d[n] == 0:
                    del d[n]
        return res
    
print(Solution().intersection([1,2,2,1], [2,2]))