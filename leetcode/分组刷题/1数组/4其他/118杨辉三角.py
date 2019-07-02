# -*- coding: utf-8 -*-
"""
Created on Wed May 29 22:11:19 2019

@author: 鱼红叶
"""


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        res = [[1]]
        if numRows == 1:
            return res
        for i in range(1, numRows):
            tmp = []
            last = res[i-1]
            tmp.append(1)
            for j in range(len(last)-1):
                tmp.append(last[j]+last[j+1])
            tmp.append(last[-1])
            res.append(tmp)
        return res
    
print(Solution().generate(5))