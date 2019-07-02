# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 后序打印二叉树（递归）
def postOrder(node):
    if not node:
        return None
    postOrder(node.left)
    postOrder(node.right)
    print(node.val)

# 后序打印二叉树（非递归）
# 使用两个栈结构
# 首先根进栈1，然后在该根的左右结点尚未进栈1时，将根从栈1出栈，推进栈2。
# 然后左结点进栈1，右结点进栈1。
# 对左右结点进行上述两步操作。先是右结点从栈1出栈，进栈2。然后左结点从栈1出栈，进栈2。
# 从而栈2形成根右左的顺序。
# 最后第二个栈依次出栈。
def postOrder2(node):
    stack = [node]
    stack2 = []
    while len(stack) > 0:
        node = stack.pop()
        stack2.append(node)
        if node.left is not None:
            stack.append(node.left)
        if node.right is not None:
            stack.append(node.right)
    while len(stack2) > 0:
        print(stack2.pop().val)

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
postOrder(node1)
print()
postOrder2(node2)