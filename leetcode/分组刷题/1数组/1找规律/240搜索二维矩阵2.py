class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        if not matrix: return False
        
        rows, cols = len(matrix)-1, len(matrix[0])-1
        i, j = rows, 0
        while i >= 0 and j <= cols:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                j += 1
            else:
                i -= 1
        return False
                