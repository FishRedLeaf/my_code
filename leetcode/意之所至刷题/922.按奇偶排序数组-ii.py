#
# @lc app=leetcode.cn id=922 lang=python3
#
# [922] 按奇偶排序数组 II
#
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        n = len(A)
        i, j = 0, 1
        while i <= n-2 and j <= n-1:
            if A[i] % 2 != 0:
                A[i], A[j] = A[j], A[i]
                j += 2
            else:
                i += 2
        return A

