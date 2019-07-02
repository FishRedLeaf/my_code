#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 递归 
    def isSymmetric(self, root: TreeNode) -> bool:
        queue = [root, root]
        while queue:
            p1 = queue.pop()
            p2 = queue.pop()
            if not p1 and not p2:
                continue
            if not p1 or not p2:
                return False
            if p1.val != p2.val:
                return False
            queue.append(p1.left)
            queue.append(p2.right)
            queue.append(p1.right)
            queue.append(p2.left)
        return True


    # 非递归 82.32 %
    # def isSymmetric(self, root: TreeNode) -> bool:
    #     return self.isMirror(root, root)
    
    # def isMirror(self, root1, root2):
    #     if not root1 and not root2:
    #         return True
    #     if not root1 or not root2:
    #         return False
    #     return root1.val == root2.val \
    #         and self.isMirror(root1.left, root2.right) \
    #         and self.isMirror(root1.right, root2.left)

