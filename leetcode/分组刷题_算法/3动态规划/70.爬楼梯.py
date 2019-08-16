#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        p2, p1, cur = 0, 1, 2
        for _ in range(3, n+1):
            tmp = p1 + cur
            p2 = p1
            p1 = cur
            cur = tmp
        return cur

