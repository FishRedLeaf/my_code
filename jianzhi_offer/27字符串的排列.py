# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 20:59:04 2019

@author: 鱼红叶

输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,
则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。

输入描述:
输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。
返回字符串列表！！！！！！！！！！！！！
"""

class Solution:
    def Permutation(self, ss):
        res = []
        if len(ss) == 0: return []
        if len(ss) == 1: return [ss]
        for i in range(len(ss)):
            prefix = ss[i]
            rest = ss[:i] + ss[i+1:]
            for j in self.Permutation(rest):
                if prefix+j not in res:
                    res.append(prefix+j)
        return res
        
    def Permutation2(self, ss):
        res = []
        if len(ss) <= 1:
            return ss
        for i in range(len(ss)):
            for j in map(lambda x: ss[i]+x, self.Permutation2(ss[:i]+ss[i+1:])):
                if j not in res:
                    res.append(j)
        return res
    
print(Solution().Permutation('abc'))