# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 21:47:42 2019

@author: 鱼红叶
"""

# leetcode 322零钱兑换

# 纯暴力
def coinChange1(coins, amount):
    if amount == 0:
        return 0
    ans = float('inf')
    for coin in coins:
        if amount - coin < 0:
            continue
        sub = coinChange1(coins, amount-coin)
        if sub == -1:
            continue
        ans = min(ans, sub+1)
    return -1 if ans == float('inf') else ans

# 暴力+备忘录
def coinChange2(coins, amount):
    def helper(coins, amount, memo):
        if amount == 0:
            return 0
        if memo[amount] != -2:
            return memo[amount]
        ans = float('inf')
        for coin in coins:
            if amount - coin < 0:
                continue
            sub = coinChange2(coins, amount-coin)
            if sub == -1:
                continue
            ans = min(ans, sub+1)
        memo[amount] = -1 if ans == float('inf') else ans
        return memo[amount]
    memo = [-2] * (amount + 1)
    return helper(coins, amount, memo)

# DP
def coinChange3(coins, amount):
    dp = [float('inf')] * (amount+1)
    dp[0] = 0
    for i in range(1, amount+1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i-coin]+1)
    return -1 if dp[amount] == float('inf') else dp[amount]

coins = [1, 2, 5]
amount = 11
print(coinChange1(coins, amount))
print(coinChange2(coins, amount))
print(coinChange3(coins, amount))