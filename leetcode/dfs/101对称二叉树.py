"""
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / `
  2   2
 / ` / `
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / `
  2   2
  `    `
   3    3
说明:

如果你可以运用递归和迭代两种方法解决这个问题，会很加分。
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        return self.symmetric(root, root)
    
    def symmetric(self, root1, root2):
        if root1 == None and root2 == None:
            return True
        if root1 == None or root2 == None:
            return False
        return root1.val == root2.val and self.symmetric(root1.left, root2.right) and self.symmetric(root1.right, root2.left)

class Solution2(object):
    def isSymmetric(self, root):
        lyst = []
        lyst.append(root)
        lyst.append(root)
        while lyst:
            root1 = lyst.pop()
            root2 = lyst.pop()
            if root1 == None and root2 == None:
                continue
            if root1 == None or root2 == None:
                return False
            if root1.val != root2.val:
                return False
            lyst.append(root1.left)
            lyst.append(root2.right)
            lyst.append(root1.right)
            lyst.append(root2.left)
        return True