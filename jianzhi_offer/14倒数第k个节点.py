# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 21:52:18 2019

@author: 鱼红叶
输入一个链表，输出该链表中倒数第k个结点。
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        p1, p2 = head, head
        for i in range(k):
            if p1 == None:
                return None
            else:
                p1 = p1.next
        if p1 == None:
            return head
        while p1.next:
            p1 = p1.next
            p2 = p2.next
        return p2.next