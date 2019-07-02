#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
# https://leetcode-cn.com/problems/course-schedule/solution/tuo-bu-pai-xu-by-liweiwei1419/
#
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0:
            return True
        
        in_degrees = [0 for _ in range(numCourses)]
        adj = [set() for _ in range(numCourses)]

        for second, first in prerequisites:
            in_degrees[second] += 1
            adj[first].add(second)
        
        queue = []
        for i in range(numCourses):
            if in_degrees[i] == 0:
                queue.append(i)
            
        counter = 0
        while queue:
            counter += 1
            cur = queue.pop(0)
            for node in adj[cur]:
                in_degrees[node] -= 1
                if in_degrees[node] == 0:
                    queue.append(node)
        return counter == numCourses



