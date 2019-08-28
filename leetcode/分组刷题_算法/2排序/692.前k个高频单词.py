#
# @lc app=leetcode.cn id=692 lang=python3
#
# [692] 前K个高频单词
#
class Solution:

    # # 堆排序
    # def topKFrequent(self, words: List[str], k: int) -> List[str]:
    #     import heapq
    #     d = {}
    #     for w in words:
    #         d[w] = d.get(w, 0) + 1
    #     lyst = [(-value, key) for key, value in d.items()]
    #     heapq.heapify(lyst)
    #     return [heapq.heappop(lyst)[1] for _ in range(k)]

    # hash+python自带sort
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = {}
        for w in words:
            d[w] = d.get(w, 0) + 1
        a = [(key, v) for key, v in d.items()]
        a.sort(key=lambda x : (-x[1], x[0]))
        return [i[0] for i in a][:k]

    # # 官方答案
    # # hash+python自带sort
    # def topKFrequent(self, words: List[str], k: int) -> List[str]:
    #     count = collections.Counter(words)
    #     candidates = count.keys()
    #     candidates.sort(key = lambda w: (-count[w], w))
    #     return candidates[:k]


