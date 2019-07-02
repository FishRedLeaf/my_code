#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 给定一个非空节点，最终路径经过这个节点有4种情况：
# 1.只有该节点本身（左右子树的路径都是负数）；
# 2.该节点+左子树路径；
# 3.该节点+右子树路径；
# 4.该节点+左子树路径+右子树路径。
# 其中1，2，3都可以作为子树路径和向上延伸，而4则不行。

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = float('-inf')
        self.maxGain(root)
        return self.res
        
    def maxGain(self, node):
        # 用于计算包含当前节点的最大路径和
        if not node:
            return 0
        left = self.maxGain(node.left)
        right = self.maxGain(node.right)
        # 这三种情况是经过node且可以向上传递的值
        tmp = node.val + max(max(left, right), 0)
        self.res = max(self.res, max(tmp, node.val+left+right))
        return tmp

