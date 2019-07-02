#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#

# 79.92% 35.74%
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        row, col = len(board), len(board[0])


        def dfs(word, i, j):
            if not word:
                return True
            if 0 <= i < row and 0 <= j < col and board[i][j] == word[0]:
                # 注：原来是使用一个visited数组去保存是否访问过的，已改进
                # 仅在寻找单词的下一个字母的时候，将当前位置设置为已访问过
                tmp = board[i][j]
                board[i][j] = 3
                flag = dfs(word[1:], i-1, j) or dfs(word[1:], i+1, j) \
                    or dfs(word[1:], i, j-1) or dfs(word[1:], i, j+1)
                # 在当前位置往外寻找word结束后，将当前位置再设置为未访问过
                # 因为对board的位置进行循环的时候，
                # 到下一个位置仍旧是用上全部的board去匹配word
                board[i][j] = tmp
                return flag
            return False


        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    if dfs(word, i, j):
                        return True
        return False

