'''
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
示例 1:

输入:
    2
   / `
  1   3
输出: true
示例 2:

输入:
    5
   / `
  1   4
     / `
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.ValidBST(root, -2**32, 2**32-1)
        
    def ValidBST(self, root, small, large):
        if not root:
            return True
        if small >= root.val or large <= root.val:
            return False
        return self.ValidBST(root.left, small, root.val) and self.ValidBST(root.right, root.val, large)
        
class Solution2(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def inorder(root):
            if not root:
                return []
            res = []
            if root.left:
                res += inorder(root.left)
            res.append(root.val)
            if root.right:
                res += inorder(root.right)
            return res
        res = inorder(root)
        return res == sorted(list(set(res)))

class Solution3(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        prev = float('-inf')
        stack = [(1, root)]
        while stack:
            p = stack.pop()
            if not p[1]:
                continue
            if p[0] == 0:
                if p[1].val <= prev:
                    return False
                prev = p[1].val
            else:
                stack.append((1, p[1].right))
                stack.append((0, p[1]))
                stack.append((1, p[1].left))
        return True