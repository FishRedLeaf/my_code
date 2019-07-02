#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 朋友圈
#

# 并查集 47.81%
# class UnionFind:
#     def __init__(self, n):
#         self.father = list(range(n))
#         # rank[i]表示以i为根节点的集合的高度
#         self.rank = [0 for i in range(n)]
#         self.count = n

#     def find(self, x):
#         father = self.father
#         if father[x] != x:
#             # 路径压缩
#             father[x] = self.find(father[x])
#         return father[x]
    
#     def union(self, x, y):
#         father, rank = self.father, self.rank
#         x, y = map(self.find, [x, y])
#         # 如果x和y根节点相同，那么属于同一个集合
#         if x == y:
#             return False
#         # 高度小的树往高度大的树上合并，
#         # 操作为高度小的树的根节点连到高度大的树的根节点
#         if rank[x] > rank[y]:
#             father[y] = x
#         else:
#             father[x] = y
#             # 高为2的树往高为3的树上合并,高为3；
#             # 高为2的树往高为2的树上合并,高为2+1；
#             if rank[x] == rank[y]:
#                 rank[y] += 1
#         self.count -= 1
#         return True

#     def get_count(self):
#         return self.count
        

# class Solution:
#     def findCircleNum(self, M: List[List[int]]) -> int:
#         uf = UnionFind(len(M))
#         for i in range(len(M)):
#             for j in range(i+1, len(M[0])):
#                 if M[i][j] == 1:
#                     uf.union(i, j)
#         return uf.get_count()

# dfs 37.05%
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        count = 0
        visited = [0 for _ in range(len(M))]
        for i in range(len(M)):
            if not visited[i]:
                count += 1
                self.dfs(M, visited, i)
        return count
    
    def dfs(self, M, visited, i):
        visited[i] = 1
        for j in range(len(M)):
            if M[i][j] and not visited[j]:
                self.dfs(M, visited, j)

