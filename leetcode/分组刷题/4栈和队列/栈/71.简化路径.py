#
# @lc app=leetcode.cn id=71 lang=python3
#
# [71] 简化路径
#
class Solution:
    def simplifyPath(self, path: str) -> str:
        s = path.split('/')
        stack = []
        for c in s:
            if c in ["", "."]:
                continue
            if c == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(c)
        return '/' + '/'.join(stack)

