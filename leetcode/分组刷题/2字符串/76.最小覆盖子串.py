#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not s or not t:
            return ""
        
        d = {}
        for c in t:
            d[c] = d.get(c, 0) + 1
        # from collections import Counter
        # d = Counter(t)
        
        l, r = 0, 0
        ans = float('inf'), None, None
        required = len(d)
        formed = 0

        window = {}
        while r < len(s):

            c = s[r]
            window[c] = window.get(c, 0) + 1
            if c in d and d[c] == window[c]:
                formed += 1

            while l <= r and required == formed:
                c = s[l]
                if r-l+1 < ans[0]:
                    ans = (r-l+1, l, r)
                window[c] -= 1
                if c in d and window[c] < d[c]:
                    formed -= 1
                l += 1
            r += 1
        return "" if ans[0] == float('inf') else s[ans[1]:ans[2]+1]


