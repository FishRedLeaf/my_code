#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        i, j, id = 0, 0, 0
        while j < len(strs) and i < len(strs[j]):
            if j == 0:
                char = strs[j][i]
            else:
                if char != strs[j][i]:
                    # 直接退出while循环
                    break
            
            if j == len(strs)-1:
                i += 1
                j = 0
                id += 1
            else:
                j += 1
        return strs[0][:id]

# print(Solution().longestCommonPrefix(["flower","flow","flight"]))