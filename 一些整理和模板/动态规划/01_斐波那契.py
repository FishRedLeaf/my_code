# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 18:26:27 2019

@author: 鱼红叶
"""

# 纯暴力递归解法，会发生重叠子问题，O(2^n)
def fib1(n):
    if n in (1, 2):
        return 1
    return fib1(n-1) + fib1(n-2)


# 带备忘录的递归解法，使用哈希表存储，解决了重叠子问题，O(n)
# 本解法自顶向下，动态规划自底向上
# 自顶向下f(20)从上到下逐渐分解为f(18),f(19)，知道f(1)和f(2)触底
def fib2(n):
    if n < 1:
        return 0
    # 备忘录
    memo = [0] * (n+1)
    def helper(n, memo):
        if n in (1,2):
            return 1
        if memo[n] != 0:
            return memo[n]
        memo[n] = helper(n-1, memo) + helper(n-2, memo)
        return memo[n]
    return helper(n, memo)


# dp
def fib3(n):
    dp = [0] * (n+1)
    dp[1] = dp[2] = 1
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# dp空间优化
def fib4(n):
    if n < 2:
        return n
    pre, cur = 0, 1
    for i in range(n-1):
        sum_ = pre + cur
        pre = cur
        cur = sum_
    return cur


import time
n = 35
stime = time.time()
print(fib1(n))
print(time.time()-stime)

stime = time.time()
print(fib2(n))
print(time.time()-stime)

stime = time.time()
print(fib3(n))
print(time.time()-stime)

stime = time.time()
print(fib4(n))
print(time.time()-stime)




