#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#
class Solution:
    def generateParenthesis(self, n):
        self.res = []
        def dfs(left, path, n):
            if len(path) == 2*n:
                if left == 0:
                    self.res.append(path)
                return
            if left < n:
                dfs(left+1, path+'(', n)
            if left > 0:
                dfs(left-1, path+')', n)
        dfs(0, '', n)
        return self.res

# print(Solution().generateParenthesis(3))
