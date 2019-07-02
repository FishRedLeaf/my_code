# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 20:22:18 2019

@author: 鱼红叶

输入一棵二叉树，求该树的深度。
从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，
最长路径的长度为树的深度。
"""

class Solution:
    def TreeDepth(self, pRoot):
        if pRoot == None:
            return 0
        return 1+max(self.TreeDepth(pRoot.left), self.TreeDepth(pRoot.right))