#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#
class Solution:
    def coinChange(self, coins, amount):
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i-coin] + 1)
            # print(dp)
        return dp[-1] if dp[-1] != float('inf') else -1

# print(Solution().coinChange([1,2,5], 11))

