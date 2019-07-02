#
# @lc app=leetcode.cn id=344 lang=python3
#
# [344] 反转字符串
#
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = len(s)
        if l == 0 or l == 1:
            return
        for i in range(l//2):
            s[i], s[l-i-1] = s[l-i-1], s[i]

