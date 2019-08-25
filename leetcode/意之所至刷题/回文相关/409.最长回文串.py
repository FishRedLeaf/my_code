#
# @lc app=leetcode.cn id=409 lang=python3
#
# [409] 最长回文串
#
class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        for c in s:
            d[c] = d.get(c, 0) + 1
        res = 0
        if_exist_one = False
        for k, v in d.items():
            res += 2 * (v // 2)
            if v % 2 == 1:
                if_exist_one = True
        if if_exist_one:
            res += 1
        return res

