# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 22:07:15 2019

@author: 鱼红叶

输入一个链表，反转链表后，输出新链表的表头。
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def ReverseList(self, pHead):
        p1, p2 = pHead, None
        while p1:
            tmp = p1.next
            p1.next = p2
            p2 = p1
            p1 = tmp
        return p1