#
# @lc app=leetcode.cn id=2 lang=python
#
# [2] 两数相加
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val + l2.val < 10:
            l3 = ListNode(l1.val+l2.val)
            l3.next = self.addTwoNumbers(l1.next, l2.next)
        else:
            tmp = ListNode(1)
            l3 = ListNode(l1.val+l2.val-10)
            l3.next = self.addTwoNumbers(self.addTwoNumbers(l1.next, tmp), l2.next)

        return l3

