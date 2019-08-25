#
# @lc app=leetcode.cn id=718 lang=python3
#
# [718] 最长重复子数组
# 注意本题的子数组(如果是字符串,那么就是子串),必须是连续的！！！
#
class Solution:
    def findLength(self, A, B):
        la, lb = len(A), len(B)
        dp = [[0] * (lb+1) for _ in range(la+1)]
        for i in range(la-1, -1, -1):
            for j in range(lb-1, -1, -1):
                if A[i] == B[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
        return max([max(row) for row in dp])

# print(Solution().findLength([1,2,3,4,1], [1,4,3,2,1]))

