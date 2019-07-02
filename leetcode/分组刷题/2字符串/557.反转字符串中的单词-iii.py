#
# @lc app=leetcode.cn id=557 lang=python3
#
# [557] 反转字符串中的单词 III
#
class Solution:
    def reverseWords(self, s: str) -> str:
        res, tmp = [], ''
        for c in s.strip():
            if c != ' ':
                tmp += c
            else:
                if tmp.strip():
                    res.append(tmp[::-1])
                    tmp = ''
        if tmp.strip():
            res.append(tmp[::-1])

        ans = ''
        for i in res:
            ans += i + ' '
        return ans[:-1]

