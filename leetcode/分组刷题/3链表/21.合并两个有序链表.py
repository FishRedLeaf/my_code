#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val > l2.val:
            l3 = ListNode(l2.val)
            l3.next = self.mergeTwoLists(l1, l2.next)
        else:
            l3 = ListNode(l1.val)
            l3.next = self.mergeTwoLists(l1.next, l2)
        return l3

