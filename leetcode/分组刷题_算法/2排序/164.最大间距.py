#
# @lc app=leetcode.cn id=164 lang=python3
#
# [164] 最大间距
#
class Solution:
    # 桶排序 46.64%
    def maximumGap(self, nums: List[int]) -> int:
        import math
        n = len(nums)
        if n < 2:
            return 0
        a, b = min(nums), max(nums)
        if a == b:
            return 0
        gap = int(math.ceil((b-a) / (n-1)))
        bucketMin = [float('inf') for _ in range(n+1)]
        bucketMax = [float('-inf') for _ in range(n+1)]
        for num in nums:
            idx = (num - a) // gap
            bucketMin[idx] = min(bucketMin[idx], num)
            bucketMax[idx] = max(bucketMax[idx], num)
        bucketMin = [i for i in bucketMin if i != float('inf')]
        bucketMax = [i for i in bucketMax if i != float('-inf')]
        ans = 0
        for i in range(len(bucketMax)-1):
            ans = max(ans, bucketMin[i+1] - bucketMax[i])
        return ans

    # 基数排序————待补充

    # # 比较排序 17%
    # def maximumGap(self, nums: List[int]) -> int:
    #     nums.sort()
    #     n = len(nums)
    #     res = 0
    #     for i in range(1, n):
    #         res = max(res, nums[i]-nums[i-1])
    #     return res

