#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#
class Solution:
    def romanToInt(self, s: str) -> int:
        ddd = {'I':1,
               'V':5,
               'X':10,
               'L':50,
               'C':100,
               'D':500,
               'M':1000}
        res = 0
        for i in range(len(s)):
            if i > 0 and ddd[s[i]] > ddd[s[i-1]]:
                res += ddd[s[i]] - 2 * ddd[s[i-1]]
            else:
                res += ddd[s[i]]
        return res

