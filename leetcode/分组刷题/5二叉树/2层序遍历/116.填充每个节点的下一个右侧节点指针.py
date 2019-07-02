#
# @lc app=leetcode.cn id=116 lang=python3
#
# [116] 填充每个节点的下一个右侧节点指针
#
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        curLayerNodes = [root]
        while curLayerNodes:
            nextLayerNodes = []
            for node in curLayerNodes:
                if node.left:
                    nextLayerNodes.append(node.left)
                if node.right:
                    nextLayerNodes.append(node.right)
            if len(curLayerNodes) > 1:
                for i in range(len(curLayerNodes)-1):
                    curLayerNodes[i].next = curLayerNodes[i+1]
            curLayerNodes = nextLayerNodes
        return root

