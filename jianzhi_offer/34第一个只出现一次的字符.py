# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 22:21:21 2019

@author: 鱼红叶

在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,
并返回它的位置, 如果没有则返回 -1（需要区分大小写）.
"""

class Solution:
    def FirstNotRepeatingChar(self, s):
        from collections import OrderedDict
        d = OrderedDict()
        for k in s:
            d[k] = d.get(k,0) + 1

        for k,v in d.items():
            if v == 1:
                return s.index(k)
        return -1