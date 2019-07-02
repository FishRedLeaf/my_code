# -*- coding: utf-8 -*-
"""
Created on Sat May 25 18:36:21 2019

@author: Administrator
"""

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)

s = "abc"
t = "ahbgdc"
print(Solution().isSubsequence(s, t))