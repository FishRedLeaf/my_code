# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 22:04:25 2019

@author: 鱼红叶

请实现一个函数按照之字形打印二叉树，
即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，
第三行按照从左到右的顺序打印，其他行以此类推。
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
        isEvenLayer = True
        while curLayerNodes:
            curLayerVals = []
            nextLayerNodes = []
            isEvenLayer = not isEvenLayer
            for node in curLayerNodes:
                curLayerVals.append(node.val)
                if node.left:
                    nextLayerNodes.append(node.left)
                if node.right:
                    nextLayerNodes.append(node.right)
            curLayerNodes = nextLayerNodes
            res.append(curLayerVals[::-1]) if isEvenLayer else res.append(curLayerVals)
        return res