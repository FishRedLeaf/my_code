#
# @lc app=leetcode.cn id=19 lang=python
#
# [19] 删除链表的倒数第N个节点
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return head

        # 正向行进n-1步到达正数第n个节点
        p = head
        for _ in range(n-1):
            p = p.next

        # 如果此时p.next为空，说明链表长度为n，那么倒数第n个节点为head
        if not p.next:
            return head.next
        
        # 
        p1 = head
        # while循环至少跑一步，因为此时p.next不为空。因此pre_p1不会未定义
        while p.next:
            p = p.next
            pre_p1 = p1
            p1 = p1.next
        pre_p1.next = p1.next

        return head
        

