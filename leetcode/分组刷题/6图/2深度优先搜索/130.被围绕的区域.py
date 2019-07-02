#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return 
        row, col = len(board), len(board[0])
        # 每个单元格都是边界的情况
        if row < 3 or col < 3:
            return
        
        def dfs(i, j):
            if 0 <= i < row and 0 <= j < col and board[i][j] == 'O':
                board[i][j] = '#'
                dfs(i-1, j)
                dfs(i+1, j)
                dfs(i, j-1)
                dfs(i, j+1)
        
        for i in range(row):
            dfs(i, 0)
            dfs(i, col-1)
        for i in range(col):
            dfs(0, i)
            dfs(row-1, i)
        
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '#':
                    board[i][j] = 'O'


