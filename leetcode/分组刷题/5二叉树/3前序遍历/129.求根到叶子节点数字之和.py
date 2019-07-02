#
# @lc app=leetcode.cn id=129 lang=python3
#
# [129] 求根到叶子节点数字之和
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 0
        stack = [(root, 0)]
        while stack:
            node, v = stack.pop()
            if not node.left and not node.right:
                res += 10*v + node.val
            if node.left:
                stack.append((node.left, 10*v+node.val))
            if node.right:
                stack.append((node.right, 10*v+node.val))
        return res

