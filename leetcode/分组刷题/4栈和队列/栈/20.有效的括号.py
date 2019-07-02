#
# @lc app=leetcode.cn id=20 lang=python
#
# [20] 有效的括号
#
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        left = ['(', '[', '{']
        right = [')', ']', '}']
        stack = []
        for c in s:
            if c in left:
                stack.append(c)
            else:
                idx = right.index(c)
                if not stack:
                    return False
                popItem = stack.pop()
                if popItem != left[idx]:
                    return False
        if not stack:
            return True
        return False 

