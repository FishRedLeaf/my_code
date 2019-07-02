class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]

        属于找规律的数组题
        用四个变量来控制边界，然后因为方向总是：→↓←↑ 左右下上
        """
        if matrix == [] : return []
        res = []
        maxUp = maxLeft = 0
        maxDown = len(matrix) - 1
        maxRight = len(matrix[0]) - 1 
        direction = 0 # 0 go right, 1 go down, 2 go left, 3 up
        while True:
            if direction == 0:
                for i in range(maxLeft, maxRight+1):
                    res.append(matrix[maxUp][i])
                maxUp += 1
            elif direction == 1:
                for i in range(maxUp, maxDown+1):
                    res.append(matrix[i][maxRight])
                maxRight -= 1
            elif direction == 2:
                for i in reversed(range(maxLeft, maxRight+1)):
                    res.append(matrix[maxDown][i])
                maxDown -= 1
            else:
                for i in reversed(range(maxUp, maxDown+1)):
                    res.append(matrix[i][maxLeft])
                maxLeft += 1
            if maxLeft > maxRight or maxUp > maxDown:
                return res
            direction = (direction + 1) % 4


matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
print(Solution().spiralOrder(matrix))
# [1, 2, 3, 6, 9, 8, 7, 4, 5]