#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#
class Solution:
    def rob(self, nums: List[int]) -> int:
        L = len(nums)
        if L == 0:
            return 0
        if L == 1:
            return nums[0]
        if L == 2:
            return max(nums[0], nums[1])
        def rob_line(nums):
            p2, p1 = 0, nums[0]
            for i in range(2, len(nums)+1):
                tmp = max(p2+nums[i-1], p1)
                p2 = p1
                p1 = tmp
            return tmp
        return max(rob_line(nums[1:]), rob_line(nums[:-1]))


