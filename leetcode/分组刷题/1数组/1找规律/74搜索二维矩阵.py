
'''
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。
'''

class Solution:
    def searchMatrix(self, matrix, target):
        '''
        先对行二分查找，再对列二分查找
        '''

        if not matrix or not matrix[0]:
            return False
        row = len(matrix)
        col = len(matrix[0]) if row else 0
        l, r = 0, row-1
        while l <= r:
            midrow = l + ((r-l) >> 1)
            if matrix[midrow][0] <= target <= matrix[midrow][col-1]:
                m, n = 0, col-1
                while m <= n:
                    midcol = m + ((n-m) >> 1)
                    if matrix[midrow][midcol] == target:
                        return True
                    elif matrix[midrow][midcol] > target:
                        n = midcol - 1
                    else:
                        m = midcol + 1
                return False
            elif matrix[midrow][0] > target:
                r = midrow - 1
            else:
                l = midrow + 1
        return False


matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
print(Solution().searchMatrix(matrix, 3))

