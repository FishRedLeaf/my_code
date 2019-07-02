#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False

        stack = [(root, 0)]
        while stack:
            node, v = stack.pop()
            if not node.left and not node.right:
                if v + node.val == sum:
                    return True
            if node.left:
                stack.append((node.left, v+node.val))
            if node.right:
                stack.append((node.right, v+node.val))
        return False

