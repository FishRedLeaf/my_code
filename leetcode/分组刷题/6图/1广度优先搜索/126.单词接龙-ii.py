#
# @lc app=leetcode.cn id=126 lang=python3
#
# [126] 单词接龙 II
# 参考 https://leetcode-cn.com/problems/word-ladder-ii/solution/bfs-level-order-traverse-by-matrix95/
# 找出所有的最短序列
# 1 首先BFS+层序遍历，停止条件为当前queue为空或者endWord在当前queue中，
# 这表示到这一层就是最短的转换序列
# 2 在遍历过程中构建字典用于后续回溯，格式为routine[next_word].append(cur_word)
# 3 回溯，注意routine[beginWord] = []，也就是routine[word]=[]时是一条符合条件的路径

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList):
        if endWord not in wordList or not beginWord or not endWord or not wordList:
            return []

        def backtrack(res, routine, path, endWord):
            if not routine[endWord]:
                res.append([endWord] + path)
            else:
                for pre in routine[endWord]:
                    backtrack(res, routine, [endWord] + path, pre)

        L = len(beginWord)
        res = []
        lookup = set([beginWord]) | set(wordList)
        routine = {word:[] for word in lookup}
        cur_queue = set([beginWord])
        while cur_queue and endWord not in cur_queue:
            next_queue = set()
            for word in cur_queue:
                lookup.remove(word)
            for word in cur_queue:
                for i in range(L):
                    for j in range(97,123):
                        next_word = word[:i] + chr(j) + word[i+1:]
                        if next_word in lookup:
                            next_queue.add(next_word)
                            routine[next_word].append(word)
            cur_queue = next_queue
        # print(routine)
        
        if cur_queue:
            backtrack(res, routine, [], endWord)
        return res

# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log","cog"]
# # routine
# #{'lot': ['hot'], 'dog': ['dot'], 'cog': ['dog', 'log'], 'log': ['lot'], 'hot': ['hit'], 'hit': [], 'dot': ['hot']}

# print(Solution().findLadders(beginWord, endWord, wordList))
