# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        paths = []
        def tranverse(root, sum, path):
            if not root:
                return
            if not root.left and not root.right:
                if root.val == sum:
                    paths.append(path+[root.val])
            if root.left:
                tranverse(root.left, sum-root.val, path+[root.val])
            if root.right:
                tranverse(root.right, sum-root.val, path+[root.val])

        tranverse(root, sum, [])
        return paths