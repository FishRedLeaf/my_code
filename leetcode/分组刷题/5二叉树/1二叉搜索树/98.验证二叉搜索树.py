#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    # 14.58%
    def isValidBST(self, root: TreeNode) -> bool:
        prev = float('-inf')
        stack = [(1, root)]

        while stack:
            p = stack.pop()
            if not p[1]:
                continue
            
            if p[0] == 0:
                if prev >= p[1].val:
                    return False
                prev = p[1].val
            else:
                stack.append((1, p[1].right))
                stack.append((0, p[1]))
                stack.append((1, p[1].left))
        return True

    # 97.54%
    # def isValidBST(self, root: TreeNode) -> bool:
    #     if not root:
    #         return True
    #     stack = []
    #     p = root
    #     res = []
    #     while p or stack:
    #         if p:
    #             stack.append(p)
    #             p = p.left
    #         else:
    #             popItem = stack.pop()
    #             res.append(popItem.val)
    #             p = popItem.right
    #     return res == sorted(res) and len(res) == len(set(res))

# root = TreeNode(5)
# a = TreeNode(1)
# b = TreeNode(4)         
# c = TreeNode(3)  
# d = TreeNode(6) 
# root.left = a
# root.right = b
# b.left = c
# b.right = d

# root = TreeNode(0)
# a = TreeNode(-1)
# root.left = a
# print(Solution().isValidBST(root))

