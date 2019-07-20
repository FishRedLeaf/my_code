#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#
class Solution:
    def topKFrequent(self, nums, k):
        d = {}
        for n in nums:
            d[n] = d.get(n, 0) + 1
        buckets = [[] for _ in range(len(nums)+1)]
        for key, value in d.items():
            buckets[value].append(key)
        res = []
        for item in buckets[::-1]:
            if item and k > 0:
                while item and k > 0:
                    res.append(item.pop())
                    k -= 1
                if k == 0:
                    return res
        return res
# print(Solution().topKFrequent([1,1,1,2,2,3], 2))
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     d = {}
    #     for n in nums:
    #         d[n] = d.get(n, 0) + 1
    #     topk = sorted(d.values())[-k:]
    #     res = []
    #     for k, v in d.items():
    #         if v in topk:
    #             res.append(k)
    #     return res

