class Solution:
    def generateMatrix(self, n: int):
        '''
        属于找规律的数组题
        用四个变量来控制边界，然后因为方向总是：→↓←↑ 左右下上
        '''

        matrix = [[0]*n for _ in range(n)]
        maxUp = maxLeft = 0
        maxDown, maxRight = n-1, n-1
        direction = 0 # 0 go right, 1 go down, 2 go left, 3 up
        cur_num = 1
        while cur_num <= n ** 2:
            if direction == 0:
                for i in range(maxLeft, maxRight+1):
                    matrix[maxUp][i] = cur_num
                    cur_num += 1
                maxUp += 1
            elif direction == 1:
                for i in range(maxUp, maxDown+1):
                    matrix[i][maxRight] = cur_num
                    cur_num += 1
                maxRight -= 1
            elif direction == 2:
                for i in reversed(range(maxLeft, maxRight+1)):
                    matrix[maxDown][i] = cur_num
                    cur_num += 1
                maxDown -= 1
            else:
                for i in reversed(range(maxUp, maxDown+1)):
                    matrix[i][maxLeft] = cur_num
                    cur_num += 1
                maxLeft += 1
            direction = (direction + 1) % 4
        return matrix


print(Solution().generateMatrix(3))
        