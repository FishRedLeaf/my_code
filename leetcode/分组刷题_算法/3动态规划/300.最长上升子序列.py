#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长上升子序列
#
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        L = len(nums)
        dp = [1] * L
        for i in range(L):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

