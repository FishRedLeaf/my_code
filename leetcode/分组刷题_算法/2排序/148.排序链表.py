#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 归并排序 55.01%
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        mid = self.getMid(head)
        l1 = head
        l2 = mid.next
        mid.next = None

        l1 = self.sortList(l1)
        l2 = self.sortList(l2)

        return self.merge(l1, l2)

    def merge(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        dummy = ListNode(-1)
        cur = dummy
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
        return dummy.next
        
    def getMid(self, head):
        if not head or not head.next:
            return None
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

# # 快排两种实现， 都超时
# class Solution:
#     def sortList(self, head: ListNode) -> ListNode:

#         if not head or not head.next:
#             return head
#         self.sort_helper(head, None)
#         return head

#     def sort_helper(self, start, end):
#         if start != end:
#             mid = self.partition(start, end)
#             self.sort_helper(start, mid)
#             self.sort_helper(mid.next, end)
        
#     def partition(self, start, end):
#         pv = start.val
#         i, j = start, start.next
#         while j != end:
#             if j.val < pv:
#                 i = i.next
#                 i.val, j.val = j.val, i.val
#             j = j.next
#         start.val, i.val = i.val, start.val
#         return i

# class Solution:
#     def sortList(self, head: ListNode) -> ListNode:
#         if not head:
#             return head
#         end = head
#         while end.next:
#             end = end.next
#         self.quickSort(head, end)
#         return head

#     def quickSort(self, start, end):
#         if start != end:
#             mid = self.partition(start, end)
#             self.quickSort(start, mid)
#             if mid.next:
#                 self.quickSort(mid.next, end)
        
#     def partition(self, start, end):
#         pv = start.val
#         i, j = start, start.next
#         while j != end.next:
#             if j.val < pv:
#                 i = i.next
#                 i.val, j.val = j.val, i.val
#             j = j.next
#         start.val, i.val = i.val, start.val
#         return i
    
