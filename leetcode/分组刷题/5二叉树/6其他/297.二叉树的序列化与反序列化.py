#
# @lc app=leetcode.cn id=297 lang=python3
#
# [297] 二叉树的序列化与反序列化
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 层序遍历

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        queue = [root]
        res = []
        while queue:
            p = queue.pop(0)
            if not p:
                res.append('None')
                continue
            else:
                res.append(str(p.val))
            queue.append(p.left)
            queue.append(p.right)
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # 注意构造和序列化时相同的流程
        data = data.split(',')
        if data[0] == 'None':
            return None
        root = TreeNode(int(data[0]))
        queue = [root]
        i = 0
        while queue and i < len(data):
            p = queue.pop(0)
            left, right = None, None
            i += 1
            if i < len(data) and data[i] != 'None':
                left = TreeNode(int(data[i]))
                queue.append(left)
            i += 1
            if i < len(data) and data[i] != 'None':
                right = TreeNode(int(data[i]))
                queue.append(right)
            p.left = left
            p.right = right
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

