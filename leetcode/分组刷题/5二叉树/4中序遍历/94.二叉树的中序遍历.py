#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 非递归 89.23 %
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        stack = []
        p = root
        while p or stack:
            if p:
                stack.append(p)
                p = p.left
            else:
                popItem = stack.pop()
                res.append(popItem.val)
                p = popItem.right
        return res

    # # 递归 89.23 %
    # def inorderTraversal(self, root: TreeNode) -> List[int]:
    #     if not root:
    #         return []
    #     res = []
    #     left = self.inorderTraversal(root.left)
    #     if left:
    #         res += left
    #     res += [root.val]
    #     right = self.inorderTraversal(root.right)
    #     if right:
    #         res += right
    #     return res

