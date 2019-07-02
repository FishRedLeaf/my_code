#
# @lc app=leetcode.cn id=61 lang=python
#
# [61] 旋转链表
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head

        c = 0
        p = head
        while p:
            p = p.next
            c += 1
        
        p = head
        k = k % c
        if k == 0:
            return head
        for _ in range(c-k-1):
            p = p.next
        
        res = p.next
        p.next = None
        p1 = res
        while p1.next:
            p1 = p1.next
        p1.next = head

        return res

