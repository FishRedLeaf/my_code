#
# @lc app=leetcode.cn id=306 lang=python3
#
# [306] 累加数
#
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        for x in range(n//2+1):
            if x > 0 and num[0] == '0':
                break
            for y in range(x+1, n):
                if y > x+1 and num[x+1] == '0':
                    break
                i, j, k = 0, x, y
                while k < n:
                    a = int(num[i:j+1])
                    b = int(num[j+1:k+1])
                    add = str(int(a + b))
                    if not num.startswith(add, k+1):
                        break
                    if len(add) + k + 1 == n:
                        return True
                    i = j+1
                    j = k
                    k = k + len(add)
        return False



