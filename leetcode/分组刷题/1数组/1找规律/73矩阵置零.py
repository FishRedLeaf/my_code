class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        为了尽可能少的使用空间，想的很细
        """
        colZeroFlag = False
        for i in range(len(matrix)):
            #检查每一行第一个元素，只要出现一个0， 那么第一列就需要标记为zero
            if matrix[i][0] == 0:
                colZeroFlag = True
            #注意仅检查了第二列到最后一列，因为第一列是否置零已经在上述if语句中考虑了
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
            '''
            对行进行遍历，
            首先检查每一行第一个元素是否为0，如果为0，那么显然第一列需要置零，
            同时这一行也应该置零，这由后续检查，发现matrix[i][0]=0则将matrix[i][j]置零
            接着检查该行第二个到最后的元素，如果为0， 那么将该行第一个元素置零，且该列第一个元素也置零
            #综合来看，第一行和第一列作为表明一行或一列元素是否置零的依据
            每行第一个元素为0，将该行的第一个元素置零，即自身，已经为0；将该列第一个元素置零，就将flag置为True
            每行其他元素为0，将该行第一个元素，该列第一个元素都置零
            
            为什么对第一行和第一列的处理不一样：
            因为第一行的状态可以根据第一列的第一个元素判断，而第一列的状态不能根据第一行的第一个元素判断，
            这是因为第一行的第一个元素被第一行的其他元素修改了，这个元素只能表明第一行是否需要置零，
            而不能表明第一列是否置零。因此需要一个额外的标志位。
            当然也可以使用colZeroFlag=False作为判断依据，效果是一样的
            '''
        
        #后向遍历的过程中，每处理完一行中的第二到最后的元素，就可以根据标志位去处理该行的第一个元素，
        #因为每行的第一个元素只能用于表明该行的其他元素是否需要置零
        for i in reversed(range(len(matrix))):
            for j in reversed(range(1, len(matrix[0]))):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if colZeroFlag:
                matrix[i][0] = 0