#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
#
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1, num2 = num1[::-1], num2[::-1]
        l1, l2 = len(num1), len(num2)
        res = [0] * (l1 + l2)
        
        for i in range(l1):
            for j in range(l2):
                res[i+j] += int(num1[i]) * int(num2[j])
#        print(res)
        ans = []
        for i in range(len(res)):
            if i < len(res)-1:
                res[i+1] += res[i] // 10
            ans.append(str(res[i]%10))
        # >1是为了保证0+0=0，让输出为'0'而不是''
        while len(ans) > 1 and ans[-1] == '0':
            ans.pop(-1)
#        print(ans)
        return ''.join(ans[::-1])

