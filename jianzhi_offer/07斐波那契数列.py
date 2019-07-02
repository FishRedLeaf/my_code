# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 16:14:26 2019

@author: 鱼红叶
大家都知道斐波那契数列，现在要求输入一个整数n，
请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39
"""

class Solution:
    def Fibonacci(self, n):
        # write code here
        if n == 0: return 0
        if n == 1 or n == 2: return 1
        pp, p = 1, 1
        cur = 0
        for i in range(3, n+1):
            cur = pp + p
            pp = p
            p = cur
        return cur

print(Solution().Fibonacci(4))