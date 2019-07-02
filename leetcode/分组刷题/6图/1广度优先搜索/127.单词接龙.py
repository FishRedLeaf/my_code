#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#
class Solution:
    # 72.09 %
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        from collections import defaultdict
        if endWord not in wordList or not beginWord or not endWord or not wordList:
            return 0

        L = len(beginWord)

        d = defaultdict(list)
        for word in wordList:
            for i in range(L):
                d[word[:i] + '*' + word[i+1:]].append(word)
        
        queue = [(beginWord, 1)]
        visited = {beginWord:True}  # set([beginWord])

        while queue:
            cur_word, level = queue.pop(0)
            for i in range(L):
                intermediate_word = cur_word[:i] + '*' + cur_word[i+1:]
                for word in d[intermediate_word]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level+1))
                d[intermediate_word] = []
        return 0

    # BFS 找遍distance=0的，再找distance=1
    # 33.41 %
    # def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    #     distance, cur = 0, [beginWord]
    #     visited, lookup = set([beginWord]), set(wordList)

    #     while cur:
    #         next_queue = []

    #         for word in cur:
    #             if word == endWord:
    #                 return 1 + distance
                
    #             for i in range(len(word)):
    #                 for j in 'abcdefghijklmnopqrstuvwxyz':
    #                     candidate = word[:i] + j + word[i+1:]
    #                     if candidate not in visited and candidate in lookup:
    #                         visited.add(candidate)
    #                         next_queue.append(candidate)
    #         distance += 1
    #         cur = next_queue
    #     return 0

