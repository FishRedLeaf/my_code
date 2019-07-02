#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层次遍历 II
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        curLayerNodes = [root]
        res = [[root.val]]
        while curLayerNodes:
            nextLayerNodes = []
            nextLayerValues = []
            for node in curLayerNodes:
                if node.left:
                    nextLayerNodes.append(node.left)
                    nextLayerValues.append(node.left.val)
                if node.right:
                    nextLayerNodes.append(node.right)
                    nextLayerValues.append(node.right.val)
            if nextLayerValues:
                res.append(nextLayerValues)
            curLayerNodes = nextLayerNodes
        return res[::-1]

