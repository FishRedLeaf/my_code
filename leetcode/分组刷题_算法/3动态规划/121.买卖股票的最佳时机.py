#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        res = 0
        pre_min = prices[0]
        for i, p in enumerate(prices):
            if i >= 1:
                res = max(res, p - pre_min)
                pre_min = min(pre_min, p)
        return res

