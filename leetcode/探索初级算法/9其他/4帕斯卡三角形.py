'''
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。



在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        res = [[1]]
        if numRows == 1:
            return res
        for i in range(1, numRows):
            tmp = []
            last = res[i-1]
            tmp.append(last[0])
            for j in range(len(last)-1):
                tmp.append(last[j]+last[j+1])
            tmp.append(last[-1])
            res.append(tmp)
        return res