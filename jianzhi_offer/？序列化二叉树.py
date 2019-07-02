# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 20:11:03 2019

@author: 鱼红叶

请实现两个函数，分别用来序列化和反序列化二叉树
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def Serialize(self, root):
        # write code here
        if not root:
            return '#'
        return str(root.val) + ',' + self.Serialize(root.left) + ',' + self.Serialize(root.right)
    
    def Deserialize(self, s):
        lyst = s.split(',')
        return self.DeserializeTree(lyst)
    
    def DeserializeTree(self, lyst):
        # write code here
        if not lyst:
            return None
        val = lyst.pop(0)
        root = None
        if val != '#':
            root = TreeNode(int(val))
            root.left = self.DeserializeTree(lyst)
            root.right = self.DeserializeTree(lyst)
        return root