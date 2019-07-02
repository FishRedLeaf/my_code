#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        pre, p = None, head
        while p:
            tmp = p.next
            p.next = pre
            pre = p
            p = tmp
        return pre

    # def reverseList(self, head: ListNode) -> ListNode:
    #     if not head:
    #         return head
    #     pre, p = head, head.next
    #     pre.next = None
    #     while p:
    #         tmp = p.next
    #         p.next = pre
    #         pre = p
    #         p = tmp
    #     return pre

            


