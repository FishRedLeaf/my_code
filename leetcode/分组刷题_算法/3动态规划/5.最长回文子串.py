#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        maxlen = 0
        n = len(s)
        pre = [0] * n
        cur = [0] * n
        
        for i in range(n):
            for j in range(i+1):
                if i - j <= 1:
                    if s[i] == s[j]:
                        cur[j] = 1
                        if maxlen < i-j+1:
                            res = s[j:i+1]
                            maxlen = i-j+1
                else:
                    if s[i] == s[j] and pre[j+1]:
                        cur[j] = 1
                        if maxlen < i-j+1:
                            res = s[j:i+1]
                            maxlen = i-j+1
            pre = cur
            cur = [0] * n
        return res

