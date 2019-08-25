#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
class Solution:
    # 中心扩展 复杂度n^2, 1
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        n = len(s)
        def expandAroundCenter(left, right):
            l, r = left, right
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1

        L, R = 0, 0
        for i in range(n):
            l1 = expandAroundCenter(i, i)
            l2 = expandAroundCenter(i, i+1)
            l = max(l1, l2)
            if l > R-L:
                L = i - (l-1) // 2
                R = i + l // 2
        return s[L:R+1]




    # # dp, 复杂度n^2, n
    # def longestPalindrome(self, s: str) -> str:
    #     n = len(s)
    #     pre = [0] * (n+1)
    #     cur = [0] * (n+1)
    #     res, maxlen = '', 0
    #     for j in range(n):
    #         for i in range(j+1):
    #             if j-i <= 1:
    #                 if s[i] == s[j]:
    #                     cur[i] = 1
    #                     if j-i+1 > maxlen:
    #                         maxlen = j-i+1
    #                         res = s[i:j+1]
    #             else:
    #                 if s[i] == s[j] and pre[i+1]:
    #                     cur[i] = 1
    #                     if j-i+1 > maxlen:
    #                         maxlen = j-i+1
    #                         res = s[i:j+1]
    #         pre = cur
    #         cur = [0] * n
    #     return res

