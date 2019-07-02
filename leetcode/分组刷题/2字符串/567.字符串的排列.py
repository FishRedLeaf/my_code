#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d = {}
        for c in s1:
            d[c] = d.get(c, 0) + 1
        window = {}
        n = len(s1)
        for i, c in enumerate(s2):
            window[c] = window.get(c, 0) + 1
            if i >= n:
                window[s2[i-n]] = window.get(s2[i-n], 0) - 1
                if window[s2[i-n]] == 0:
                    del window[s2[i-n]]
            if window == d:
                return True
        return False
    
    # 超时解法
    # def checkInclusion(self, s1: str, s2: str) -> bool:
    #     l1, l2 = len(s1), len(s2)
    #     if l1 > l2:
    #         return False
    #     s1 = sorted(s1)
    #     for i in range(l2-l1+1):
    #         if s1 == sorted(s2[i:i+l1]):
    #             return True
    #     return False

    # 这对应子序列包含问题的解
    # def checkInclusion(self, s1: str, s2: str) -> bool:
    #     d = {}
    #     for c in s1:
    #         d[c] = d.get(c, 0) + 1
    #     for c in s2:
    #         if c in d:
    #             d[c] -= 1
    #             if d[c] == 0:
    #                 d.pop(c)
    #     return True if not d else False
