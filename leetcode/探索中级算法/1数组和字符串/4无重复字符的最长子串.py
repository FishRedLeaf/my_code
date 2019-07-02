'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ddd = {}
        start = 0
        ans = 0
        for i, c in enumerate(s):
            if c in ddd:
                start = max(start, ddd.get(c)+1)
            ddd[c] = i
            ans = max(ans, i-start+1)
        return ans

    def lengthOfLongestSubstring2(self, s: str) -> int:
        #长度可变的window
        #字典的k:v为元素:最新索引，最新索引指的是遍历到当前位置时，上一个出现该元素的地方
        #window右边是当前字符，
        #如果下一个字符没有在字典中，那么直接加进window，即新的max_subseq_len=i-start+1
        #如果下一个字符在字典中，那么比较它在字典中的值和window_start，
        #如果小于start，那么window当前的start不变，否则它在字典中索引的下一个位置为新的start
        maps = {}
        l, start, n = 0, 0, len(s)
        for i in range(n):
            start = max(start, maps.get(s[i],-1)+1)
            l = max(l, i-start+1)
            maps[s[i]] = i
        return l

print(Solution().lengthOfLongestSubstring("pwwkew"))