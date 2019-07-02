#
# @lc app=leetcode.cn id=684 lang=python3
#
# [684] 冗余连接
#
class Solution:

    # 97.7 %
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = list(range(len(edges)+1))

        def get_parent(node):
            if parents[node] == node:
                return node
            else:
                return get_parent(parents[node])
        
        for e in edges:
            p1 = get_parent(e[0])
            p2 = get_parent(e[1])
            if p1 == p2:
                return e
            parents[p2] = p1
        return []


