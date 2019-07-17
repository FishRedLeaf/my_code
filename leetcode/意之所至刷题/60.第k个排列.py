#
# @lc app=leetcode.cn id=60 lang=python3
#
# [60] 第k个排列
# https://www.cnblogs.com/ariel-dreamland/p/9149577.html
import math
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        visited = [0 for _ in range(n)]
        fact = [math.factorial(n-i-1) for i in range(n)]
        ans = ''
        k -= 1
        for i in range(n):
            t = k // fact[i]
            for j in range(n):
                if not visited[j]:
                    if t == 0:
                        break
                    t -= 1
            k %= fact[i]
            ans += str(j + 1)
            visited[j] = 1
        return ans

                    

