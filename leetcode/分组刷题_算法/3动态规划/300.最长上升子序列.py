#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长上升子序列
#
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        cells = [nums[0]]
        for num in nums[1:]:
            if num > cells[-1]:
                cells.append(num)
                continue
            l, r = 0, len(cells)-1
            while l < r:
                mid = l + ((r-l) >> 1)
                if cells[mid] < num:
                    l = mid + 1
                else:
                    r = mid
            cells[l] = num
        return len(cells)
    
    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     if not nums:
    #         return 0
    #     L = len(nums)
    #     dp = [1] * L
    #     for i in range(L):
    #         for j in range(i):
    #             if nums[i] > nums[j]:
    #                 dp[i] = max(dp[i], dp[j] + 1)
    #     return max(dp)

