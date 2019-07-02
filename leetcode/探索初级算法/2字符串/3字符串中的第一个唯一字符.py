'''
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

案例:

s = "leetcode"
返回 0.

s = "loveleetcode",
返回 2.
 

注意事项：您可以假定该字符串只包含小写字母。
'''

class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import OrderedDict
        ddd = OrderedDict()
        for c in s:
            ddd[c] = ddd.get(c, 0) + 1
        for k,v in ddd.items():
            if v == 1:
                return s.index(k)
        return -1

    def firstUniqChar2(self, s: str) -> int:
        ddd = {}
        for c in s:
            ddd[c] = ddd.get(c, 0) + 1
        for i in range(len(s)):
            if ddd[s[i]] == 1:
                return i
        return -1

    def firstUniqChar3(self, s: str) -> int:
        letters = [0] * 26
        for c in s:
            ci = ord(c) - ord('a')
            letters[ci] += 1
        for i in range(0, len(s)):
            ci = ord(s[i]) - ord('a')
            if letters[ci] == 1:
                return i
        return -1
print(Solution().firstUniqChar3("loveleetcode"))