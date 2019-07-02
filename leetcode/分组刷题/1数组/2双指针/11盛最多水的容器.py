# -*- coding: utf-8 -*-
"""
Created on Mon May 27 21:12:59 2019

@author: 鱼红叶
"""

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        max_ = 0
        i, j = 0, len(height)-1
        while i < j:
            max_ = max(max_, (j-i) * min(height[i], height[j]))
            if height[i] < height[j] :
                i += 1
            else:
                j -= 1
        return max_
    
print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))