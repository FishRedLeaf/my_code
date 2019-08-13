class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        res = 0
        L = len(M)
        visited = set()
        def dfs(i):
            for j in range(L):
                if M[i][j] and j not in visited:
                    visited.add(j)
                    dfs(j)
        for i in range(L):
            if i not in visited:
                res += 1
                dfs(i)
        return res

M = [[1,1,0],
[1,1,0],
[0,0,1]]
print(Solution().findCircleNum(M))