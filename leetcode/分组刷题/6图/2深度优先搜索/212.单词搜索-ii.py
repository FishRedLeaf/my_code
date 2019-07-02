#
# @lc app=leetcode.cn id=212 lang=python3
#
# [212] 单词搜索 II
#

# 45.36% 92.96%
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = {}
        for word in words:
            node = root
            for letter in word:
                node = node.setdefault(letter, {})
            node['isWord'] = True
        
        row = len(board)
        col = len(board[0])
        res = []

        def dfs(i, j, word, node):
            if 0 <= i < row and 0 <= j < col and board[i][j] in node:
                node = node[board[i][j]]
                word += board[i][j]
                if 'isWord' in node:
                    res.append(word)
                tmp = board[i][j]
                board[i][j] = 3
                dfs(i-1, j, word, node)
                dfs(i+1, j, word, node)
                dfs(i, j-1, word, node)
                dfs(i, j+1, word, node)
                board[i][j] = tmp
        
        for i in range(row):
            for j in range(col):
                if board[i][j] in root:
                    dfs(i, j, "", root)

        return list(set(res))

# 84.7% 33.8%
# class TrieNode:
#     def __init__(self):
#         self.childs = {}
#         self.isWord = False

# class Trie:
#     def __init__(self):
#         self.root = TrieNode()
    
#     def insert(self, word):
#         node = self.root
#         for letter in word:
#             child = node.childs.get(letter)
#             if not child:
#                 child = TrieNode()
#                 node.childs[letter] = child
#             node = child
#         node.isWord = True

# class Solution:
#     def findWords(self, board, words):

#         row = len(board)
#         col = len(board[0])
#         res = []

#         def dfs(i, j, word, node):
#             if 0 <= i < row and 0 <= j < col and board[i][j] in node.childs:
#                 node = node.childs[board[i][j]]
#                 word += board[i][j]
#                 if node.isWord:
#                     res.append(word)
#                 tmp = board[i][j]
#                 board[i][j] = 3
#                 dfs(i-1, j, word, node)
#                 dfs(i+1, j, word, node)
#                 dfs(i, j-1, word, node)
#                 dfs(i, j+1, word, node)
#                 board[i][j] = tmp
                
#         head_unique = set()
#         root = Trie()
#         for word in words:
#             root.insert(word)
#             head_unique.add(word[0])
            
#         for i in range(row):
#             for j in range(col):
#                 if board[i][j] in head_unique:
#                     dfs(i, j, "", root.root)
                    
#         return list(set(res))

# board = [['a', 'a']]
# words = ['aaa']
# print(Solution().findWords(board, words))

