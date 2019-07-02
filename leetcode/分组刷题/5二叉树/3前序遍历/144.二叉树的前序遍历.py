#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 非递归 46.14%
    # def preorderTraversal(self, root: TreeNode) -> List[int]:
    #     if not root:
    #         return []
    #     res = []
    #     stack = [root]
    #     while stack:
    #         node = stack.pop()
    #         res.append(node.val)
    #         if node.right:
    #             stack.append(node.right)
    #         if node.left:
    #             stack.append(node.left)
    #     return res
    
    # 递归 80.44%
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = [root.val]
        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)
        if left:
            res += left
        if right:
            res += right
        return res

