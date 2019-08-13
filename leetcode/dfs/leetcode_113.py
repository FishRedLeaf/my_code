# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 16:00:39 2019

@author: gmw

给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        # 边界条件1
        if not root:
            return []
        # 边界条件2
        if not root.left and not root.right:
            if root.val == sum:
                return [[root.val]]
        # 一般情况
        res = []
        self.dfs(root, res, root.val, sum, [root.val])
        return res

    def dfs(self, node, res, current, target, path):
        for child in [node.left, node.right]:
            if self.is_valid(child):
                if self.match(current, target, child):
                    res.append(path+[child.val])
                else:
                    self.dfs(child, res, current+child.val, target, path+[child.val])

    # 判断当前节点是否合法
    def is_valid(self, node):
        if node:
            return True
        return False

    # 判断当前状态是否满足目标条件
    def match(self, current, target, child):
        if not child.left and not child.right and current+child.val == target:
            return True
        return False