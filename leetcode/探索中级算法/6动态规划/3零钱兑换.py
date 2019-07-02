'''
给定不同面额的硬币 coins 和一个总金额 amount。
编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

示例 1:

输入: coins = [1, 2, 5], amount = 11
输出: 3 
解释: 11 = 5 + 5 + 1
示例 2:

输入: coins = [2], amount = 3
输出: -1
说明:
你可以认为每种硬币的数量是无限的。
'''

# 递推方程式: dp[i] = min(dp[i], dp[i-vj]+1)， vj 是硬币的面额， 
# 组成金额a需要的硬币个数等于1+min(dp[i-vj]) 每种硬币少一个的情况下的最小值

class Solution:
    def coinChange(self, coins, amount) -> int:
        dp = [float("inf")] * (amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                if i-coin >= 0:
                    dp[i] = min(dp[i], dp[i-coin]+1)
        return dp[-1] if dp[-1] != float("inf") else -1