#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        lp = len(p)
        dict_p = {}
        for c in p:
            dict_p[c] = dict_p.get(c, 0) + 1

        dict_window = {}
        res = []
        for i, c in enumerate(s):
            dict_window[c] = dict_window.get(c, 0) + 1
            if i >= lp:
                dict_window[s[i-lp]] -= 1
                if dict_window[s[i-lp]] == 0:
                    del dict_window[s[i-lp]]
            if dict_window == dict_p:
                res.append(i-lp+1)
        return res

    # def findAnagrams(self, s: str, p: str) -> List[int]:
    #     p = sorted(p)
    #     res = []
    #     for i in range(len(s) - len(p) + 1):
    #         if sorted(s[i:i+len(p)]) == p:
    #             res.append(i)
    #     return res

