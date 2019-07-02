#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 96.54 %
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return res[::-1]

    # 递归 16.83 %
    # def postorderTraversal(self, root: TreeNode) -> List[int]:
    #     res = []
    #     if not root:
    #         return res
    #     left = self.postorderTraversal(root.left)
    #     if left:
    #         res += left
    #     right = self.postorderTraversal(root.right)
    #     if right:
    #         res += right
    #     res += [root.val]
    #     return res


