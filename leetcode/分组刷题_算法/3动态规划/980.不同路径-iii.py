#
# @lc app=leetcode.cn id=980 lang=python3
#
# [980] 不同路径 III
# https://blog.csdn.net/qq_17550379/article/details/86589259

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        p = 1
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start = (i, j)
                elif grid[i][j] == 2:
                    end = (i, j)
                elif grid[i][j] == 0:
                    p += 1
        def dfs(i, j, p):
            if not (0 <= i < m and 0 <= j < n and grid[i][j] >= 0):
                return 0
            if end == (i, j) and p == 0:
                return 1
            tmp = grid[i][j]
            grid[i][j] = -1
            res = dfs(i-1, j, p-1) + dfs(i+1, j, p-1) \
                + dfs(i, j-1, p-1) + dfs(i, j+1, p-1)
            grid[i][j] = tmp
            return res
            
        return dfs(start[0], start[1], p)

