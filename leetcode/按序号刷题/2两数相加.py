# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 11:23:47 2019

@author: 鱼红叶

给出两个 非空 的链表用来表示两个非负的整数。
其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2
        if not l2: return l1
        
        if l1.val + l2.val < 10:
            l3 = ListNode(l1.val+l2.val)
            l3.next = self.addTwoNumbers(l1.next,l2.next)
        
        if l1.val + l2.val >= 10:
            tmp = ListNode(1)
            l3 = ListNode(l1.val+l2.val-10)
            l3.next = self.addTwoNumbers(self.addTwoNumbers(l1.next,tmp), l2.next)
            
        return l3