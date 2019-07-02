#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        res = ''
        num1, num2 = num1[::-1], num2[::-1]
        l = max(len(num1), len(num2))
        if len(num1) < l:
            num1 += '0' * (l-len(num1))
        else:
            num2 += '0' * (l-len(num2))
#        print(num1, num2)
        c = 0
        for i in range(l):
            n = int(num1[i]) + int(num2[i]) + c
            res += str(n)[-1]
            c = n // 10
#            print(res, c)
        if c != 0:
            res += str(c)
        return res[::-1]

