# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 19:34:45 2019

@author: 鱼红叶

输入一颗二叉树的跟节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
(注意: 在返回值的list中，数组长度大的数组靠前)
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
         
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        if not root:
            return []
        if root and not root.left and not root.right and root.val == expectNumber:
            return [[root.val]]
        res = []
        left = self.FindPath(root.left, expectNumber-root.val)
        right = self.FindPath(root.right, expectNumber-root.val)
        for i in left+right:
            res.append([root.val] + i)
        return res

class Solution2:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        ret = [] # 存放结果,结果是一个二维变量
        path = [] # 存放走过的路径
        self.Find(root, expectNumber, ret, path)
        return ret
     
    def Find(self, root, target, ret, path):
        if not root:#递归结束的条件
            return
        # 走到叶子结点的情况,保存路径
        isLeaf = (root.left is None and root.right is None)
        if isLeaf and target == root.val:
            ret.append(path)  # 这里这一步要千万注意啊，
            # 假如是:ret.append(path), 结果是错的。因为Python可变对象都是引用传递啊。
        if root.left:
            self.Find(root.left, target - root.val, ret, path+[root.val])
        if root.right:
            self.Find(root.right, target - root.val, ret, path+[root.val])