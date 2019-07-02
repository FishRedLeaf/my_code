# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 15:44:01 2019

@author: 鱼红叶

输入两棵二叉树A，B，判断B是不是A的子结构。
ps：我们约定空树不是任意一个树的子结构
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        res = False
        if pRoot1 and pRoot2:
            if pRoot1.val == pRoot2.val:
                res = self.DoesTree1HaveTree2(pRoot1, pRoot2)
            if not res:
                res = self.HasSubtree(pRoot1.left, pRoot2)
            if not res:
                res = self.HasSubtree(pRoot1.right, pRoot2)
        return res
    
    def DoesTree1HaveTree2(self, pRoot1, pRoot2):
        if not pRoot2:
            return True
        if not pRoot1:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return self.DoesTree1HaveTree2(pRoot1.left,pRoot2.left) and self.DoesTree1HaveTree2(pRoot1.right, pRoot2.right)