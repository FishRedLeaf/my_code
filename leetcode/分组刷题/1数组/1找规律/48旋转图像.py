class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 1 将矩阵进行上下翻转
        # 2 将矩阵沿着轴对角线轴对称的元素交换

        rows, cols = len(matrix), len(matrix[0])

        for i in range(rows//2):
            matrix[i], matrix[rows-i-1] = matrix[rows-i-1], matrix[i]

        print(matrix)
        
        for i in range(rows):
            for j in range(i+1, cols):
                print(i,j)
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
Solution().rotate(matrix)
print(matrix)