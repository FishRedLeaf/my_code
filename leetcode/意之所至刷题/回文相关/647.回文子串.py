#
# @lc app=leetcode.cn id=647 lang=python3
#
# [647] 回文子串
#
class Solution:
    # 91.83%
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        def expandAroundCenter(left, right):
            l, r = left, right
            count = 0
            while l >= 0 and r < n and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            return count

        res = 0
        for i in range(n):
            c1 = expandAroundCenter(i, i)
            c2 = expandAroundCenter(i, i+1)
            res += c1 + c2
        return res

    # 8.53%
    # def countSubstrings(self, s: str) -> int:
    #     n = len(s)
    #     dp = [0] * (n+1)
    #     for i in range(n):
    #         count = 0
    #         for j in range(i+1):
    #             if s[j:i+1] == s[j:i+1][::-1]:
    #                 count += 1
    #         dp[i+1] = count + dp[i]
    #     return dp[-1]

