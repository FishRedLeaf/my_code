'''
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:

输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
说明：

所有输入均为小写字母。
不考虑答案输出的顺序。
'''

class Solution(object):
    def groupAnagrams2(self, strs):
        ddd = {} #"aet" : ["ate","eat","tea"] 键为最小序
        for s in strs:
            key = ''.join(sorted(list(s)))
            if key in ddd:
                ddd[key].append(s)
            else:
                ddd[key] = [s]
        return ddd.values()
        
    #笨比方法，超时
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ddd = [{} for _ in range(len(strs))]
        for i, s in enumerate(strs):
            for c in s:
                ddd[i][c] = ddd[i].get(c, 0) + 1
        
        unique_ddd = []
        for d in ddd:
            if d not in unique_ddd:
                unique_ddd.append(d)
        res = []
        for d1 in unique_ddd:
            tmp = []
            for i, d2 in enumerate(ddd):
                if d1 == d2:
                    tmp.append(strs[i])
            res.append(tmp)
        return res

    