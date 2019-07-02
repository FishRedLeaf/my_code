# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 21:22:43 2019

@author: 鱼红叶

数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。
如果不存在则输出0。
"""

class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        dict_ = {}
        for i in range(len(numbers)):
            dict_[numbers[i]] = dict_.get(numbers[i],0) + 1
        #import collections
        #dict_ = collections.Counter(numbers)
        x = len(numbers) // 2
        for k,v in dict_.items():
            if v > x:
                return k
        return 0