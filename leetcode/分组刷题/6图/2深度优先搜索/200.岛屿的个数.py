#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿的个数
#
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    self.dfs(grid, i, j)
        return count

    def dfs(self, grid, i, j):
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
            grid[i][j] = '0'
            self.dfs(grid, i-1, j)
            self.dfs(grid, i, j-1)
            self.dfs(grid, i+1, j)
            self.dfs(grid, i, j+1)

