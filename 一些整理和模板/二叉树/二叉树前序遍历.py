# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 前序打印二叉树（递归）
def preOrder(node):
    if not node:
        return None
    print(node.val)
    preOrder(node.left)
    preOrder(node.right)

# 前序打印二叉树（非递归）
def preOrder2(node):
    stack = [node]
    while len(stack) > 0:
        node = stack.pop()
        print(node.val)
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)

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
preOrder(node1)
print()
preOrder2(node2)