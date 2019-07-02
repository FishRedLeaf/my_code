#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
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
        
        pre, p = ListNode(None), head
        while p:
            if pre.val != p.val:
                pre = p
                p = p.next
            else:
                p = p.next
                pre.next = p
            
        return head

