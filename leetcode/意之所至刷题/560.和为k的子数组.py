#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为K的子数组
#
class Solution:
    def subarraySum(self, nums, k):
        preSum = ans = 0
        visit = {0: 1}
        for i, n in enumerate(nums):
            # print(visit)
            preSum += n
            # preSum-k在数组visit中，说明preSum-k对应全?个元素
            # 从?+1个元素到当前元素的连续子数组的和为k
            ans += visit.get(preSum - k, 0)
            # 以[1,1,-2,2], k=2为例
            # 遍历到1,1时，preSum=2,visit[preSum-k]=1
            # 这对应1,1这个连续子数组
            # 遍历到1,1,-2,2时,preSum=2,visit[preSum-k]=2
            # 这对应1,1,-2,2和2这两个连续子数组
            visit[preSum] = visit.get(preSum, 0) + 1
            # visit: {0: 2, 1: 1, 2: 2}
        print(visit)
        return ans

print(Solution().subarraySum([1,1,-2,2], 2))  # 3
# 1,1; 1,1,-2,2; 2

