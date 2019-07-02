'''
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
说明:

如果你可以运用递归和迭代两种方法解决这个问题，会很加分。
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#递归版本
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.symmetric(root, root)
        
    def symmetric(self, root1, root2):
        if root1 == None and root2 == None:
            return True
        if root1 == None or root2 == None:
            return False
        if root1 and root2 and root1.val != root2.val:
            return False
        return self.symmetric(root1.left, root2.right) and self.symmetric(root1.right, root2.left)

class Solution2(object):
     def isSymmetric(self, root: TreeNode) -> bool:
        if not root : 
            return True
        qlist=[root.left, root.right]
        while len(qlist)!=0:
            t1=qlist.pop()
            t2=qlist.pop()
            if not t1 and not t2: continue
            if not t1 or not t2: return False
            if t1.val != t2.val : return False
            qlist.append(t1.left)
            qlist.append(t2.right)
            qlist.append(t1.right)
            qlist.append(t2.left)
        return True