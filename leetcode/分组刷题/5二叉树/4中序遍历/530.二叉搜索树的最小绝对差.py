#
# @lc app=leetcode.cn id=530 lang=python3
#
# [530] 二叉搜索树的最小绝对差
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        ans = float('inf')
        lastval = None
        stack = []
        node = root
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                if lastval is not None:
                    ans = min(ans, abs(lastval - node.val))
                lastval = node.val
                node = node.right
        return ans

# a = TreeNode(0)
# b = TreeNode(2236)
# c = TreeNode(1277)
# d = TreeNode(2776)
# e = TreeNode(519)
# a.right = b
# b.left = c
# b.right = d
# c.left = e
# print(Solution().getMinimumDifference(a))

