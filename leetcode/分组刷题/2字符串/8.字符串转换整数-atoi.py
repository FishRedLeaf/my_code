#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()

        num = 0
        if len(s) == 0:
            return 0
        
        Positive = True
        if s[0] == '+' or s[0] == '-':
            if s[0] == '-':
                Positive = False
            s = s[1:]
        
        for c in s:
            if c >= '0' and c <= '9':
                num = 10 * num + ord(c) - ord('0')
            else:
                break
        
        if num > 2**31-1:
            if Positive:
                return 2**31-1
            else:
                return -2**31
        
        if Positive:
            return num
        return -num

