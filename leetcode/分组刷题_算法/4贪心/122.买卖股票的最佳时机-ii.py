#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        res = 0
        for i in range(1, n):
            if prices[i] > prices[i-1]:
                res += prices[i] - prices[i-1]
        return res

