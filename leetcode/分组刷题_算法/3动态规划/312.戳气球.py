#
# @lc app=leetcode.cn id=312 lang=python3
#
# [312] 戳气球
# https://leetcode-cn.com/problems/burst-balloons/solution/python-dp-yuan-lian-jie-httpsleetcodecomproblemsbu/
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        # dp[i][j]表示从戳破i+1到j-1的气球的最大收益，
        # 完成后，i+1~j-1之间的气球都没了
        dp = [[0] * n for _ in range(n)]

        for j in range(2, n):
            for i in range(j-2, -1, -1):
                for k in range(i+1, j):
                    # 假设最后删除的是气球k，那么此时i+1~k-1和k+1~j-1的气球都没了，
                    # 此时戳破气球k的收益为nums[i]*nums[k]*nums[j]
                    dp[i][j] = max(dp[i][j], dp[i][k]+dp[k][j]+nums[i]*nums[k]*nums[j])
        '''
        dp[i][j]依赖于dp[i][k]和dp[k][j]
        k在i+1~j-1之间
        k < j => j依赖于之前的信息
        k > i => i依赖于之后的信息
        为保证遍历到(i,j)时，需要的子问题的解都已经求得，
        j从前往后遍历，i从后往前遍历
        '''
        return dp[0][-1]

