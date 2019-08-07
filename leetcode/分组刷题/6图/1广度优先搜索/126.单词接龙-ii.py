#
# @lc app=leetcode.cn id=126 lang=python3
#
# [126] 单词接龙 II
# Solution参考 https://leetcode-cn.com/problems/word-ladder-ii/solution/bfs-level-order-traverse-by-matrix95/
# Solution2在此基础上改进
# Solution 30%
# Solution2 73%
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
        print(routine)
        
        if cur_queue:
            backtrack(res, routine, [], endWord)
        return res

class Solution2(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        if not beginWord or not endWord or not wordList:
            return 0
        L = len(beginWord)
        
        def backtrack(res, routine, path, endWord):
            if not routine[endWord]:
                res.append([endWord] + path)
            else:
                for pre in routine[endWord]:
                    backtrack(res, routine, [endWord]+path, pre)
        
        from collections import defaultdict
        d = defaultdict(list)
        for word in wordList:
            for i in range(L):
                d[word[:i] + '*' + word[i+1:]].append(word)
        
        cur_queue = set([beginWord])
        lookup = set([beginWord]) | set(wordList)
        routine = {word:[] for word in lookup}
        res = []
        while cur_queue and endWord not in cur_queue:
            next_queue = set()
            for word in cur_queue:
                lookup.remove(word)
            for word in cur_queue:
                for i in range(L):
                    intermediate = word[:i] + '*' + word[i+1:]
                    for next_word in d[intermediate]:
                        if next_word in lookup:
                            next_queue.add(next_word)
                            routine[next_word].append(word)
            cur_queue = next_queue
        print(routine)
        print(cur_queue)
        # 非常关键，因为层序遍历的条件有两个，
        # 停止条件为当前queue为空或者endWord在当前queue中
        # 必须是endWord在当前quque中，即存在合适的转换序列时，才需要进行回溯
        if cur_queue:  # 非常关键，
            backtrack(res, routine, [], endWord)       
        return res

beginWord = "hot"
endWord = "dog"
wordList = ["hot","dog"]
print(Solution().findLadders(beginWord, endWord, wordList))

# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log","cog"]
# # routine
# #{'lot': ['hot'], 'dog': ['dot'], 'cog': ['dog', 'log'], 'log': ['lot'], 'hot': ['hit'], 'hit': [], 'dot': ['hot']}

# print(Solution().findLadders(beginWord, endWord, wordList))
