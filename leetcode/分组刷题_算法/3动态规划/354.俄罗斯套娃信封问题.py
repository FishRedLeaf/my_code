#
# @lc app=leetcode.cn id=354 lang=python3
#
# [354] 俄罗斯套娃信封问题
#

from bisect import bisect_left
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        if n < 2:
            return n
        envelopes = sorted(envelopes, key=lambda a : (a[0], -a[1]))
        # LIS
        nums = [envelopes[i][1] for i in range(n)]
        cells = [nums[0]]
        for num in nums[1:]:
            if num > cells[-1]:
                cells.append(num)
                continue
            l, r = 0, len(cells)-1
            while l < r:
                mid = l + ((r-l)>>1)
                if cells[mid] < num:
                    l = mid + 1
                else:
                    r = mid
            cells[l] = num
        return len(cells)
    
    # # 超时
    # def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
    #     if not envelopes:
    #         return 0
    #     # [[wi, hi]] 对w升序，w相同则对h降序
    #     envelopes = sorted(envelopes, key=lambda a : (a[0], -a[1]))
    #     # LIS
    #     n = len(envelopes)
    #     dp = [1] * n
    #     for i in range(n):
    #         for j in range(i):
    #             if envelopes[i][1] > envelopes[j][1]:
    #                 dp[i] = max(dp[i], dp[j]+1)
    #     return max(dp)


