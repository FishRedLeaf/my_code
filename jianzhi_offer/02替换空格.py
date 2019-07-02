# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 12:56:07 2019

@author: 鱼红叶

请实现一个函数，将一个字符串中的每个空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
"""

class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        
        count = 0
        for i in s:
            if i == ' ':
                count += 1
                
        newStrLen = len(s) + count * 2
        newStr = ['a'] * newStrLen
        
        i, j = newStrLen-1, len(s)-1
        while i>=0 and j>=0:
            if s[j] != ' ':
                newStr[i] = s[j]
                i -= 1
                j -= 1
            else:
                newStr[i-2:i+1] = "%20"
                i -= 3
                j -= 1
        res = ''.join(newStr)
        return res
    
s = Solution()
print(s.replaceSpace("aaa sss ddd"))