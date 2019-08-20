#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i + j > 0:
                    if i == 0:
                        dp[i][j] = dp[i][j-1]
                    elif j == 0:
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

