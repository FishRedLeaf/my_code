# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 20:03:23 2019

@author: 鱼红叶
输入一个复杂链表
（每个节点中有节点值，以及两个指针，一个指向下一个节点，
另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。
（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
"""

class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
         
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if pHead == None:
            return None
        self.cloneNodes(pHead)
        self.ConnectRandomNodes(pHead)
        return self.reconstructNodes(pHead)
    
    def cloneNodes(self, pHead):
        pNode = pHead
        while pNode:
            tmp = RandomListNode(pNode.label)
            tmp.next = pNode.next
            pNode.next = tmp
            pNode = tmp.next
    
    def ConnectRandomNodes(self, pHead):
        pNode = pHead
        while pNode:
            pCloned = pNode.next
            if pNode.random != None:
                pCloned.random = pNode.random.next
            pNode = pCloned.next
        
    def reconstructNodes(self, pHead):
        pNode = pHead
        pClonedHead = pClonedNode = pNode.next
        pNode.next = pClonedNode.next
        pNode = pNode.next
        
        while pNode:
            pClonedNode.next = pNode.next
            pClonedNode = pClonedNode.next
            pNode.next = pClonedNode.next
            pNode = pNode.next
        return pClonedHead
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        