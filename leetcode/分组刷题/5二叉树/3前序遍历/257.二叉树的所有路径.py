#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []
        if not root:
            return res
        
        stack = [(root, [])]
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                res.append('->'.join(path+[str(node.val)]))
            if node.right:
                stack.append((node.right, path+[str(node.val)]))
            if node.left:
                stack.append((node.left, path+[str(node.val)]))
        return res

