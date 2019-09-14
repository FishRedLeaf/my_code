
"""
参考：
https://leetcode-cn.com/problems/course-schedule/solution/course-schedule-tuo-bu-pai-xu-bfsdfsliang-chong-fa/
https://leetcode-cn.com/problems/course-schedule/solution/tuo-bu-pai-xu-by-liweiwei1419/
"""

# 以课程表为模板

"""
BFS
1 构建入度表
2 使用队列queue，将入度为0的节点全部入队
3 当queue非空，依次将队首节点出队，在课程安排图中删除此节点 pre(每次入度减1，当入度为0时删除pre)
4 在每次pre出队后，执行numCourses-1

"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        indegrees = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adj[pre].append(cur)
        queue = []
        for i in range(numCourses):
            if indegrees[i] == 0:
                queue.append(i)
        while queue:
            node = queue.pop()
            numCourses -= 1
            for cur in adj[node]:
                indegrees[cur] -= 1
                if indegrees[cur] == 0:
                    queue.append(cur)
        return numCourses == 0

"""
DFS 判断图中是否有环
0,-1,1分别表示未被访问过，被访问过确认该节点不属于任何一个环，当前dfs正在访问的节点
"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        if len(prerequisites) < 1:
            return True

        def dfs(i):
            if visited[i] == -1: return True
            if visited[i] == 1: return False
            visited[i] = 1
            # 如果一个节点的所有前导节点都不构成环，那么当前节点也不构成环
            # 如果一个节点的所有后继节点都不构成环，那么当前节点也不构成环
            for j in inverse_adj[i]:
                if not dfs(j):  return False
            visited[i] = -1
            return True

        visited = [0] * numCourses
        inverse_adj = [[] for _ in range(numCourses)]
        for cur, pre in prerequisites:
            # adj[pre].append(cur)
            inverse_adj[cur].append(pre)
        for i in range(numCourses):
            if not dfs(i): return False
        return True


# 课程表2
# BFS
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return list(range(numCourses))
        res = []
        indegrees = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adj[pre].append(cur)
        queue = []
        for i in range(numCourses):
            if indegrees[i] == 0:
                queue.append(i)
        while queue:
            node = queue.pop()
            res.append(node)
            numCourses -= 1
            for cur in adj[node]:
                indegrees[cur] -= 1
                if indegrees[cur] == 0:
                    queue.append(cur)
        if numCourses == 0:
            return res
        return []

# DFS
# 体会回溯！！！
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        if not prerequisites:
            return list(range(numCourses))

        visited = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        for cur, pre in prerequisites:
            adj[pre].append(cur)

        res = []
        def dfs(i):
            if visited[i] == -1: return True
            if visited[i] == 1: return False
            visited[i] = 1
            # res中先加入了j，而i -> j，所以最终需要反转res，或者adj改为inverse_adj
            for j in adj[i]:
                if not dfs(j): return False
            visited[i] = -1
            res.append(i)
            return True

        for i in range(numCourses):
            if not dfs(i): return []
        return res[::-1]

# 另一个DFS实现
# https://leetcode-cn.com/problems/course-schedule-ii/solution/ke-cheng-biao-ii-by-leetcode/
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return list(range(numCourses))

        visited = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        for cur, pre in prerequisites:
            adj[pre].append(cur)

        res = []
        is_possible = True

        def dfs(i):
            nonlocal is_possible
            if not is_possible:
                return
            visited[i] = 1
            for j in adj[i]:
                if visited[j] == 0:
                    dfs(j)
                elif visited[j] == 1:
                    is_possible = False
            visited[i] = -1
            res.append(i)

        for i in range(numCourses):
            if visited[i] == 0:
                dfs(i)
        return res[::-1] if is_possible else []