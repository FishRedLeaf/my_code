#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层次遍历
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        curLayerNodes = [root]
        res = [[root.val]]
        isEven = False
        while curLayerNodes:
            nextLayerNodes = []
            nextLayerValues = []
            isEven = not isEven
            for node in curLayerNodes:
                if node.left:
                    nextLayerNodes.append(node.left)
                    nextLayerValues.append(node.left.val)
                if node.right:
                    nextLayerNodes.append(node.right)
                    nextLayerValues.append(node.right.val)
            if nextLayerValues:
                res.append(nextLayerValues[::-1]) if isEven else res.append(nextLayerValues)
            curLayerNodes = nextLayerNodes
        return res

