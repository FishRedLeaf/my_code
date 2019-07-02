# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 16:25:09 2019

@author: 鱼红叶
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
"""

class Solution:
    def rectCover(self, number):
        if number <= 0: return 0
        if number == 1: return 1
        if number == 2: return 2
        alist = [1,2]
        for i in range(2,number):
            alist.append(alist[i-1]+alist[i-2])
        return alist[-1]