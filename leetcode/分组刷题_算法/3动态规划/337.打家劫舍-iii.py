#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        def dfs(root):
            if not root:
                return 0, 0
            # 当前节点最终确定的最大值(考虑了不包含和包含当前节点两种情况)，不包含当前节点的最大值
            lpre, lppre = dfs(root.left)
            rpre, rppre = dfs(root.right)
            # 不包含当前节点，取左子节点的最大值和右子节点的最大值直接相加
            # 包含当前节点，取左边不包含左子节点的最大值和右边不包含右子节点的最大值，再加上当前节点的值
            return max(root.val+lppre+rppre, lpre+rpre), lpre+rpre
        return dfs(root)[0]
            
    # def rob(self, root: TreeNode) -> int:
    #     def dfs(root):
    #         # 返回值: (不包含当前节点的最大值，包含当前节点的最大值)
    #         if not root:
    #             return (0, 0)
    #         l0, l1 = dfs(root.left)
    #         r0, r1 = dfs(root.right)
    #         res0 = max(l0, l1) + max(r0, r1)
    #         res1 = l0 + r0 + root.val
    #         return (res0, res1)
    #     res = dfs(root)
    #     return max(res[0], res[1])

