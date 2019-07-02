# -*- coding: utf-8 -*-
"""
Created on Wed May 29 21:52:43 2019

@author: 鱼红叶
"""

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        intervals.sort(key = lambda x: x.start)
        res = []
        for interval in intervals:
            if res and res[-1].end >= interval.start:
                res[-1].end = max(res[-1].end, interval.end)
            else:
                res.append(interval)
        return res