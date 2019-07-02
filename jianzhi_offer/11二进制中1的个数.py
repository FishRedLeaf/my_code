# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 16:29:27 2019

@author: 鱼红叶
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
python中int范围无限，
本题对其限制一下，-2^31 ~ 2^31-1 负数用补码形式
1111fffffff ~ 0111ffff-1

思路：
找出32位中1的个数
"""

class Solution:
    def NumberOf1(self, n):
        count = 0
        bit = 1
        INT_BITS = 32
        MAX_INT = (1 << (INT_BITS-1)) - 1
        #for _ in range(32):
        while bit <= MAX_INT+1:
            if n & bit:
                count += 1
            bit <<= 1
        return count