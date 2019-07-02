# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 21:57:25 2019

@author: 鱼红叶

从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def Print(self, pRoot):
        res = []
        if not pRoot:
            return res
        curLayerNodes = [pRoot]
        while curLayerNodes:
            curLayerVals = []
            nextLayerNodes = []
            for node in curLayerNodes:
                curLayerVals.append(node.val)
                if node.left:
                    nextLayerNodes.append(node.left)
                if node.right:
                    nextLayerNodes.append(node.right)
            curLayerNodes = nextLayerNodes
            res.append(curLayerVals)
        return res