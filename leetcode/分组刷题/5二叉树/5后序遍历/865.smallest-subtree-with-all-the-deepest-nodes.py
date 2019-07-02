#
# @lc app=leetcode.cn id=865 lang=python3
#
# [865] Smallest Subtree with all the Deepest Nodes
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        if left == right:
            return root
        if left > right:
            return self.subtreeWithAllDeepest(root.left)
        return self.subtreeWithAllDeepest(root.right)
        
    def maxDepth(self, root):
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

