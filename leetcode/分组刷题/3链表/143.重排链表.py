#
# @lc app=leetcode.cn id=143 lang=python3
#
# [143] 重排链表
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# def printListNode(head):
#     while head:
#         print(head.val, end=' ')
#         head = head.next
#     print()

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        # 1 2 3 4 5
        p1, p2 = head, head.next
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
            
        # p1: 3, p: 4
        pre, p = None, p1.next
        # 4 5 -> 5 4
        p1.next = None
        while p:
            tmp = p.next
            p.next = pre
            pre = p
            p = tmp
        
        # p: None, p1: 5
        while head and pre:
            tmp = pre.next
            pre.next = head.next
            head.next = pre
            head = pre.next
            pre = tmp
# head = ListNode(1)
# a = ListNode(2)
# b = ListNode(3)
# c = ListNode(4)
# d = ListNode(5)
# head.next = a
# a.next = b
# b.next = c
# c.next = d

# Solution().reorderList(head)

# printListNode(head)

