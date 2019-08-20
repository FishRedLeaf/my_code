#
# @lc app=leetcode.cn id=518 lang=python3
#
# [518] 零钱兑换 II
#
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount+1)
        dp[0] = 1
        for coin in coins:
            for i in range(amount+1):
                if i+coin <= amount:
                    dp[i+coin] += dp[i]
        return dp[-1]

