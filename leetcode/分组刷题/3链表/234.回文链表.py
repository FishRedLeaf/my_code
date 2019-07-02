#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # e.g. 1->2->3->4->5->NULL

        if not head:
            return True

        p1, p2 = head, head.next
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
        # p1 = 3
        # 反转p1->……->NULL,3->4->5->NULL
        p = p1.next
        p1.next = None
        while p:
            tmp = p.next
            p.next = p1
            p1 = p
            p = tmp
        # 5->4->3
        while p1 and head:
            if p1.val != head.val:
                return False
            p1 = p1.next
            head = head.next
        return True


# a = ListNode(1)
# a.next = ListNode(2)
# print(Solution().isPalindrome(a))
