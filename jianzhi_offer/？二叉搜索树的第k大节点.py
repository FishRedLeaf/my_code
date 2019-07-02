# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 20:34:45 2019

@author: 鱼红叶

给定一棵二叉搜索树，请找出其中的第k小的结点。
例如， （5，3，7，2，4，6，8）    中，按结点数值大小顺序第三小结点的值为4。
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    # 返回对应节点TreeNode
    def __init__(self):
        self.count = 0
        
    def KthNode(self, pRoot, k):
        if not pRoot:
            return None
        node = self.KthNode(pRoot.left, k)
        if node:
            return node
        self.count += 1
        if self.count == k:
            return pRoot
        node = self.KthNode(pRoot.right, k)
        if node:
            return node