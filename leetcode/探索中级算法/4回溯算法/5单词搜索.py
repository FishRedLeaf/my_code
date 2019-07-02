'''
给定一个二维网格和一个单词，找出该单词是否存在于网格中。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。
同一个单元格内的字母不允许被重复使用。

示例:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true.
给定 word = "SEE", 返回 true.
给定 word = "ABCB", 返回 false.
'''

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows, cols = len(board), len(board[0])
        visited = [[0]*cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if not visited[i][j]:
                    if self.backtrack(board, visited, word, i, j):
                        return True
        return False
    
    def backtrack(self, board, visited, word, i, j):
        rows, cols = len(board), len(board[0])
        if not word:
            return True
        if 0 <= i < rows and 0 <= j < cols:
            if visited[i][j] == 0 and board[i][j] == word[0]:
                visited[i][j] = 1
                flag = self.backtrack(board, visited, word[1:], i-1, j) or self.backtrack(board, visited, word[1:], i+1, j) or self.backtrack(board, visited, word[1:], i, j+1) or self.backtrack(board, visited, word[1:], i, j-1)
                visited[i][j] = 0
                return flag
            else:
                return False
        else:
            return False

board =[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
print(Solution().exist(board, "ABCCED"))