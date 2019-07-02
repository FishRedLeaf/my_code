#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 95.58 %
    def isBalanced(self, root: TreeNode) -> bool:
        self.flag = True

        def maxDepth(root):
            if not root:
                return 0
            left = maxDepth(root.left)
            right = maxDepth(root.right)
            if abs(left - right) > 1:
                self.flag = False
            return 1 + max(left, right)

        maxDepth(root)
        return True if self.flag else False

    # 10.48 %
    # def isBalanced(self, root: TreeNode) -> bool:
    #     if not root:
    #         return True
    #     left = self.maxDepth(root.left)
    #     right = self.maxDepth(root.right)
    #     if abs(left - right) > 1:
    #         return False
    #     return self.isBalanced(root.left) and self.isBalanced(root.right)

    # def maxDepth(self, root):
    #     if not root:
    #         return 0
    #     return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        

