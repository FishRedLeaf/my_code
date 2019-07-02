#
# @lc app=leetcode.cn id=160 lang=python
#
# [160] 相交链表
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p1, p2 = headA, headB
        c1, c2 = 0, 0
        while p1:
            p1 = p1.next
            c1 += 1
        while p2:
            p2 = p2.next
            c2 += 1
        
        if c1 > c2:
            for _ in range(c1-c2):
                headA = headA.next
        else:
            for _ in range(c2-c1):
                headB = headB.next
        
        while headA != headB:
            headA = headA.next
            headB = headB.next

        return headA

