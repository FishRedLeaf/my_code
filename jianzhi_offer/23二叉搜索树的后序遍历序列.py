# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 15:26:13 2019

@author: 鱼红叶

输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
"""

class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if sequence == []:
            return False
        root = sequence[-1]

        #找到序列中第一个比sequence[-1]大的数，如果没有右子树设置为len(sequence)-1
        right_start = len(sequence)-1
        for i in range(len(sequence)-1):
            if sequence[i] > root:
                right_start = i
                break
        
        for i in range(right_start, len(sequence)-1):
            if sequence[i] < root:
                return False
        
        left = True
        #左子树不为空
        if right_start > 0:
            left = self.VerifySquenceOfBST(sequence[:right_start])
        right = True
        if right_start < len(sequence)-1:
            right = self.VerifySquenceOfBST(sequence[right_start:-1])
        
        return left and right
        
print(Solution().VerifySquenceOfBST([2,3,4]))