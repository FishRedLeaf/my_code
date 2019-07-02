#
# @lc app=leetcode.cn id=138 lang=python
#
# [138] 复制带随机指针的链表
#
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """

        if not head:
            return head
            
        p = head
        while p:
            tmp = Node(p.val, p.next, None)
            p.next = tmp
            p = tmp.next
        
        p = head
        while p:
            p.next.random = p.random.next if p.random else None
            p = p.next.next
        
        p = head
        p1 = p.next
        res = p1
        while p:
            p.next = p1.next
            p = p.next
            p1.next = p.next if p else None
            p1 = p1.next
        return res
            

