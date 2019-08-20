#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        res = 0
        start = 0
        for i, c in enumerate(s):
            if c in d:
                start = max(start, d[c]+1)
            res = max(res, i-start+1)
            d[c] = i
        return res

