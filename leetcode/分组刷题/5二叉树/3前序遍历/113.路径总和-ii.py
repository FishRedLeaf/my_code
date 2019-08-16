#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        def dfs(node, v, path):
            if not node:
                return 
            if not node.left and not node.right and v + node.val == sum:
                res.append(path+[node.val])
                return
            dfs(node.left, v+node.val, path+[node.val])
            dfs(node.right, v+node.val, path+[node.val])
        dfs(root, 0, [])
        return res

