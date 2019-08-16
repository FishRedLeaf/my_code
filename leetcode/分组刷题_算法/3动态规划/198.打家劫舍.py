#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#
# https://www.cnblogs.com/grandyang/p/4383632.html
# dp[i] = max(num[i] + dp[i - 2], dp[i - 1])
class Solution:
    def rob(self, nums):
        L = len(nums)
        if L <= 0:
            return 0
        if L == 1:
            return nums[0]

        # 89.59%
        p2, p1 = 0, nums[0]
        for i in range(2, L+1):
            tmp = max(p2+nums[i-1], p1)
            p2 = p1
            p1 = tmp
        return tmp

        # 54.57%
        # dp = [0] * (L+1)
        # dp[1] = nums[0]
        # for i in range(2, L+1):
        #     dp[i] = max(dp[i-2]+nums[i-1], dp[i-1])
        # return dp[-1]

# print(Solution().rob([1,2,3,1]))

