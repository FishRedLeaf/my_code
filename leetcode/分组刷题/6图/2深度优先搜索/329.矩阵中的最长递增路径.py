#
# @lc app=leetcode.cn id=329 lang=python3
#
# [329] 矩阵中的最长递增路径
#
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        if not matrix:
            return 0
            
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        row = len(matrix)
        col = len(matrix[0])

        def dfs(i, j, visited, cache):
            if (i, j) in visited:
                return visited[(i, j)]
            
            res = 0
            for di, dj in directions:
                p, q = i + di, j + dj
                if p < 0 or q < 0 or p >= row or q >= col:
                    continue
                if (p, q) not in cache and matrix[p][q] > matrix[i][j]:
                    cache.add((p, q))
                    r = dfs(p, q, visited, cache)
                    res = max(res, r)
                    cache.discard((p, q))
            visited[(i, j)] = 1 + res
            return 1 + res

        ans = 0
        visited = {}
        cache = set()
        for i in range(row):
            for j in range(col):
                cache.add((i, j))
                res = dfs(i, j, visited, cache)
                ans = max(ans, res)
                cache.discard((i, j))
        return ans

