#
# @lc app=leetcode.cn id=892 lang=python3
#
# [892] 三维形体的表面积
#
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        N = len(grid)
        ans = 0
        for i in range(N):
            for j in range(N):
                if grid[i][j]:
                    ans += 2
                    neighbors = ((i-1, j), (i+1, j), (i, j-1), (i, j+1))
                    for ii, jj in neighbors:
                        if 0 <= ii < N and 0 <= jj < N:
                            nval = grid[ii][jj]
                        else:
                            nval = 0
                        ans += max(grid[i][j]-nval, 0)
        return ans

