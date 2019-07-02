# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 22:25:08 2019

@author: 鱼红叶

输入两个单调递增的链表，输出两个链表合成后的链表，
当然我们需要合成后的链表满足单调不减规则。
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def Merge(self, pHead1, pHead2):
        if not pHead1: return pHead2
        if not pHead2: return pHead1
        
        p = None
        if pHead1.val < pHead2.val:
            p = pHead1
            p.next = self.Merge(pHead1.next, pHead2)
        else:
            p = pHead2
            p.next = self.Merge(pHead1, pHead2.next)
        return p
            