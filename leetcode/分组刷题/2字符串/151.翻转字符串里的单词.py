#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 翻转字符串里的单词
#
class Solution:
    def reverseWords(self, s: str) -> str:
        res, tmp = [], ''
        for c in s.strip():
            if c != ' ':
                tmp += c
            else:
                if tmp.strip():
                    res.append(tmp)
                    tmp = ''
        if tmp.strip():
            res.append(tmp)

        ans = ''
        for i in res[::-1]:
            ans += i + ' '
        return ans[:-1]


