# -*- coding: utf-8 -*-
"""
Created on Mon May 27 21:47:58 2019

@author: 鱼红叶
"""

class Solution:
    def merge(self, nums1, m, nums2, n):
        if m == 0:
            nums1[:] = nums2
        elif n == 0:
            return
        else:
            p1, p2, p = m-1, n-1, m+n-1
            while p1 >= 0 and p2 >= 0:
                if nums1[p1] > nums2[p2]:
                    nums1[p] = nums1[p1]
                    p1 -= 1
                else:
                    nums1[p] = nums2[p2]
                    p2 -= 1
                p -= 1
            while p2 != -1:
                nums1[p] = nums2[p2]
                p -= 1
                p2 -= 1