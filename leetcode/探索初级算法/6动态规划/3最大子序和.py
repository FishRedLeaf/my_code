'''
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
'''

class Solution:
    #f(n) = max(f(n-1) + A[n], A[n]) -> f(n) means 当前子序列的subSum
    def maxSubArray(self, nums):
        res = float('-inf')
        subSum = 0
        for n in nums:
            subSum = max(subSum+n, n)
            res = max(res, subSum)
        return res

print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) #4 -1 2 1