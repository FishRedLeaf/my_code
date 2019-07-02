# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 22:19:33 2019

@author: 鱼红叶
"""

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
#            print(slow, fast)
            if slow == fast:
                break
        
        finder = 0
        while True:
            slow = nums[slow]
            finder = nums[finder]
            print(slow, finder)
            if slow == finder:
                return slow
            
print(Solution().findDuplicate([1,3,4,2,2]))

