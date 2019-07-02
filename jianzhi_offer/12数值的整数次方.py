# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 16:13:56 2019

@author: 鱼红叶

给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
"""

class Solution:
    def Power(self, base, exponent):
        if exponent == 0:
            return 1
        if exponent == 1:
            return base
        if exponent == -1:
            return 1.0 / base
        
        res = self.Power(base, exponent >> 1)
        res *= res
        if exponent & 1 == 1:
            res *= base
        return res