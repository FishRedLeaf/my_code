'''
给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:

输入: [10,9,2,5,3,7,101,18]
输出: 4
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
说明:

可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?
'''

class Solution:
    def lengthOfLIS(self, nums) -> int:
        if not nums: 
            return 0
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            # 在nums[0]~nums[i-1]中找比nums[i]小的数，
            # 且找出其中最大的那个，假设索引为k,则dp[i] = dp[k]+1
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

print(Solution().lengthOfLIS([10,9,2,5,3,7,101,18]))