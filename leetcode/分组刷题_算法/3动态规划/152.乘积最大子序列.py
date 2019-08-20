#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子序列
# https://leetcode-cn.com/problems/maximum-product-subarray/solution/duo-chong-si-lu-qiu-jie-by-powcai-3/

class Solution:
    
    # def maxProduct(self, nums):
    #     premax, premin = nums[0], nums[0]
    #     res = nums[0]
    #     for i, n in enumerate(nums):
    #         if i >= 1:
    #             curmax = max(premax*n, premin*n, n)
    #             curmin = min(premax*n, premin*n, n)
    #             res = max(res, curmax)
    #             premax, premin = curmax, curmin
    #     return res
    
    def maxProduct(self, nums: List[int]) -> int:
        maxdp = [nums[0] for _ in range(len(nums))]
        mindp = [nums[0] for _ in range(len(nums))]
        for i in range(1, len(nums)):
            maxdp[i] = max(maxdp[i-1]*nums[i], mindp[i-1]*nums[i], nums[i])
            mindp[i] = min(maxdp[i-1]*nums[i], mindp[i-1]*nums[i], nums[i])
        return max(maxdp)

# print(Solution().maxProduct([2,3,-2,4]))
