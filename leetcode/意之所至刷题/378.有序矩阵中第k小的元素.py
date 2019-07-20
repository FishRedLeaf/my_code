#
# @lc app=leetcode.cn id=378 lang=python3
#
# [378] 有序矩阵中第K小的元素
#

# 二分 83.73%
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        L = matrix[0][0]
        R = matrix[n-1][n-1]
        res = 0
        while L <= R:
            mid = L + ((R - L) >> 1)
            if self.helper(matrix, mid, n, k):
                res = mid
                L = mid + 1
            else:
                R = mid - 1
        return res
        
    def helper(self, matrix, m, n, k):
        sum_ = 0
        for i in range(n):
            l, r, ans = 0, n-1, 0
            while l <= r:
                mid = l + ((r - l) >> 1)
                if matrix[i][mid] < m:
                    ans = mid + 1
                    l = mid + 1
                else:
                    r = mid - 1
            sum_ += ans
        return k > sum_

# # 堆排序 超时
# import heapq
# class Solution:
#     def kthSmallest(self, matrix, k):
#         visited = [{0,0}]
#         heap = [(matrix[0][0], (0,0))]
#         heapq.heapify(heap)
#         n = len(matrix)

#         while heap:
#             val, (i, j) = heapq.heappop(heap)
#             k -= 1
#             if k == 0:
#                 return val
#             if i+1 < n and (i+1, j) not in visited:
#                 heapq.heappush(heap, (matrix[i+1][j], (i+1, j)))
#                 visited.append((i+1, j))
#             if j+1 < n and (i, j+1) not in visited:
#                 heapq.heappush(heap, (matrix[i][j+1], (i, j+1)))
#                 visited.append((i, j+1))


