'''
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。
'''

class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        i, j, end = 0, 0, 0
        while j < len(strs) and i < len(strs[j]):
            if j == 0:
                char = strs[j][i]
            else:
                if char != strs[j][i]:
                    break
            
            if j == len(strs)-1:
                i += 1
                j = 0
                end += 1
            else:
                j += 1
        return strs[0][:end]
        