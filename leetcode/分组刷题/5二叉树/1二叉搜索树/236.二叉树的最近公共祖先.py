#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # 如果lp和rp都是非空，则返回当前节点（当前节点就是最近祖先）
        # left和right有一个为空，返回非空的那个。
        # 不存在全部非空,因为必有公共祖先
        if left and right:
            return root
        return left if not right else right

    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
    #     def recurse(cur_node):
    #         if not cur_node:
    #             return False
    #         left = recurse(cur_node.left)
    #         right = recurse(cur_node.right)
    #         mid = cur_node == p or cur_node == q

    #         if mid + left + right >= 2:
    #             self.ans = cur_node

    #         return mid or left or right
        
    #     recurse(root)
    #     return self.ans

