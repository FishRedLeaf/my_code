#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        import re
        s = re.sub('[^0-9A-Za-z]', '' , s)
        return s.lower() == s.lower()[::-1]

