# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 14:29:42 2019

@author: 鱼红叶

从上往下打印出二叉树的每个节点，同层节点从左至右打印。
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        if not root:
            return None
        deque, res = [], []
        deque.append(root)
        while len(deque) > 0:
            curNode = deque.pop(0)
            res.append(curNode.val)
            if curNode.left:
                deque.append(curNode.left)
            if curNode.right:
                deque.append(curNode.right)
        return res
            