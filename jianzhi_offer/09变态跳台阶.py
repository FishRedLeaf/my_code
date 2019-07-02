# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 16:22:09 2019

@author: 鱼红叶
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。
求该青蛙跳上一个n级的台阶总共有多少种跳法。
"""

class Solution:
    def jumpFloorII(self, number):
        if number <= 0: return 0
        if number == 1: return 1
        if number == 2: return 2
        alist = [1,2]
        for i in range(2,number):
            alist.append(sum(alist)+1)
        return alist[-1]
print(Solution().jumpFloorII(3))