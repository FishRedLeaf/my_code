#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#
class Solution:

    # 使用26个字母的列表作为哈希值
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())
    
    # 使用字母排列的最小序作为每个字符串的哈希值
    # def groupAnagrams2(self, strs):
    #     """
    #     :type strs: List[str]
    #     :rtype: List[List[str]]
    #     """
    #     ddd = {} #"aet" : ["ate","eat","tea"] 键为最小序
    #     for s in strs:
    #         key = ''.join(sorted(list(s)))
    #         if key in ddd:
    #             ddd[key].append(s)
    #         else:
    #             ddd[key] = [s]
    #     return ddd.values()

    # 超时
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     l = len(strs)
    #     d = [{} for _ in range(l)]
    #     for i in range(l):
    #         s = strs[i]
    #         for c in s:
    #             d[i][c] = d[i].get(c, 0) + 1
    #     unique_d = []
    #     for k in d:
    #         if k in unique_d:
    #             continue
    #         else:
    #             unique_d.append(k)
    #     res = [[] for _ in range(len(unique_d))]
    #     for i in range(l):
    #         idx = unique_d.index(d[i])
    #         res[idx].append(strs[i])
    #     return res

