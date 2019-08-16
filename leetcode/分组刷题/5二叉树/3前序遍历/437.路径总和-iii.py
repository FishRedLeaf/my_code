#
# @lc app=leetcode.cn id=437 lang=python3
#
# [437] 路径总和 III
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        self.count = 0
        d = {0 : 1}
        
        def dfs(node, pathsum, d):
            if node:
                pathsum += node.val
                self.count += d.get(pathsum-sum, 0)
                d[pathsum] = d.get(pathsum, 0) + 1
                dfs(node.left, pathsum, d)
                dfs(node.right, pathsum, d)
                d[pathsum] -= 1
        
        dfs(root, 0, d)
        return self.count


