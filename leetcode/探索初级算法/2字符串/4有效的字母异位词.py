'''
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的一个字母异位词。

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false
说明:
你可以假设字符串只包含小写字母。

进阶:
如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1, d2 = {}, {}
        for c in s:
            d1[c] = d1.get(c, 0) + 1
        for c in t:
            d2[c] = d2.get(c, 0) + 1
        return d1 == d2

    def isAnagram2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        charCount = [0 for _ in range(26)]
        for i in range(len(s)):
            charCount[ord(s[i])-ord('a')] += 1
            charCount[ord(t[i])-ord('a')] -= 1
        
        for cnt in charCount:
            if cnt != 0:
                return False
        return True