#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float('-inf')
        subsum = 0
        for n in nums:
            subsum = max(subsum+n, n)
            ans = max(ans, subsum)
        return ans


