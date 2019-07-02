#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现strStr()
#
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        l1, l2 = len(haystack), len(needle)
        if l2 > l1:
            return -1
        for i in range(l1-l2+1):
            if needle == haystack[i:i+l2]:
                return i
        return -1

