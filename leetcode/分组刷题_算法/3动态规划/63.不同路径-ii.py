#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[1] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j]:
                    dp[i][j] = 0
                else:
                    if i + j > 0:
                        if i == 0:
                            dp[i][j] = dp[i][j-1]
                        elif j == 0:
                            dp[i][j] = dp[i-1][j]
                        else:
                            dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

