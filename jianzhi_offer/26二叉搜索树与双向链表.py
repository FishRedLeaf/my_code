# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 20:22:13 2019

@author: 鱼红叶

输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
要求不能创建任何新的结点，只能调整树中结点指针的指向。
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
         
class Solution:
    def __init__(self):
        self.pHead = None
        self.pNode = None
        
    def Convert(self, pRootOfTree):
        if pRootOfTree == None:
            return None
        self.Convert(pRootOfTree.left)
        if self.pHead == None:
            self.pHead = pRootOfTree
            self.pNode = pRootOfTree
        else:
            self.pNode.right = pRootOfTree
            pRootOfTree.left = self.pNode
            self.pNode = pRootOfTree
        self.Convert(pRootOfTree.right)
        return self.pHead