#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        dummy = ListNode(-1)
        dummy.next = head

        pre, p = dummy, head
        while p:
            duplicate = False
            while p.next and p.val == p.next.val:
                p = p.next
                duplicate = True
            if duplicate:
                pre.next = p.next
            else:
                pre = p
            p = p.next

        return dummy.next

