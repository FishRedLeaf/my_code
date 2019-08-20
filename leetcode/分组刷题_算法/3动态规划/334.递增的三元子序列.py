#
# @lc app=leetcode.cn id=334 lang=python3
#
# [334] 递增的三元子序列
#
class Solution:
    # 贪心
    def increasingTriplet(self, nums: List[int]) -> bool:
        a, b = float('inf'), float('inf')
        for n in nums:
            if a >= n:
                a = n
            elif b >= n:  # a < n <= b
                b = n
            else:
                return True
        return False


    # dp超时
    # def increasingTriplet(self, nums: List[int]) -> bool:
    #     dp = [1] * len(nums)
    #     for i, n in enumerate(nums):
    #         for j in range(i):
    #             if n > nums[j]:
    #                 dp[i] = max(dp[i], dp[j]+1)
    #                 if dp[i] == 3:
    #                     return True
    #     return False

