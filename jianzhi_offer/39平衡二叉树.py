# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 20:45:21 2019

@author: 鱼红叶

输入一棵二叉树，判断该二叉树是否是平衡二叉树。
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def IsBalanced_Solution(self, pRoot):
        if pRoot == None:
            return True
        if abs(self.TreePath(pRoot.left) - self.TreePath(pRoot.right)) > 1:
            return False
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)
        
    def TreePath(self, pRoot):
        if pRoot == None:
            return 0
        nleft = self.TreePath(pRoot.left)
        nright = self.TreePath(pRoot.right)
        return 1+max(nleft, nright)