# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 中序打印二叉树（递归）
def inOrder(node):
    if not node:
        return None
    inOrder(node.left)
    print(node.val)
    inOrder(node.right)

# 中序打印二叉树（非递归）
# 在每一个节点处进行检查，如果有
def inOrder2(node):
    if not node:
        return
    stack = []
    pos = node #当前检查的节点
    while pos or stack:
        if pos:
            stack.append(pos)
            pos = pos.left
        else:
            pos = stack.pop()
            print(pos.val)
            pos = pos.right


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
g = TreeNode(7)
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g

node1, node2 = a, a
inOrder(node1)
print()
inOrder2(node2)









