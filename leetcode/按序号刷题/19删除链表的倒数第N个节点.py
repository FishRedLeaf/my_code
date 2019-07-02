# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 11:22:04 2019

@author: 鱼红叶

给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明:给定的 n 保证是有效的。
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p = head
        for _ in range(n-1):
            p = p.next
        
        if not p.next:
            return head.next
        
        p2 = head
        p2_last = p2
        while p.next:
            p = p.next
            p2_last = p2
            p2 = p2.next
        p2_last.next = p2.next
        return head
    
    def removeNthFromEnd2(self, head: ListNode, n: int) -> ListNode:
        p1 = head
        for _ in range(n):
            p1 = p1.next
        
        if not p1:
            return head.next
        
        p2 = head
        while p1.next:
            p1 = p1.next
            p2 = p2.next
        p2.next = p2.next.next
        return head
        