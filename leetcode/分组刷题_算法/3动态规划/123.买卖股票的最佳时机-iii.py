#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#
class Solution:
    # 36.45%
    def maxProfit(self, prices):
        buy1, buy2 = float('-inf'), float('-inf')
        sell1, sell2 = 0, 0
        for i in prices:
            buy1 = max(buy1, -i)
            sell1 = max(sell1, buy1+i)
            buy2 = max(buy2, sell1-i)
            sell2 = max(sell2, buy2+i)
        return sell2

    # 68.48%
    # def maxProfit(self, prices: List[int]) -> int:
    #     n = len(prices)
    #     if n < 2:
    #         return 0
        
    #     pre_min = prices[0]
    #     pre_max_profit = [0] * n
    #     for i in range(1, n):
    #         pre_max_profit[i] = max(pre_max_profit[i-1], prices[i]-pre_min)
    #         pre_min = min(pre_min, prices[i])

    #     post_max = prices[n-1]
    #     post_max_profit = [0] * n
    #     for i in range(n-2, -1, -1):
    #         post_max_profit[i] = max(post_max_profit[i+1], post_max-prices[i])
    #         post_max = max(post_max, prices[i])
        
    #     res = 0
    #     for i in range(n):
    #         res = max(res, pre_max_profit[i]+post_max_profit[i])
    #     return res

