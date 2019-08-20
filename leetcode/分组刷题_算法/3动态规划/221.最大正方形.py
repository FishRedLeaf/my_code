#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ans = 0
        if not matrix:
            return ans
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * (cols+1) for _ in range(rows+1)]
        for i in range(1, rows+1):
            for j in range(1, cols+1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                    ans = max(ans, dp[i][j])
        return ans ** 2


