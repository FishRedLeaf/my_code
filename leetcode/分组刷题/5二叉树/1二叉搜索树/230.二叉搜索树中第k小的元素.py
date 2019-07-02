#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] 二叉搜索树中第K小的元素
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        p = root
        while p or stack:
            if p:
                stack.append(p)
                p = p.left
            else:
                popItem = stack.pop()
                k -= 1
                if k == 0:
                    return popItem.val
                p = popItem.right
        
