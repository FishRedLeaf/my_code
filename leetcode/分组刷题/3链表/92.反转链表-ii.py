#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        """
        1->2->3->4->5->NULL
        dummy->1->2->3->4->5->NULL
        m=2,n=4
        dummy->1-> 2<-3-<4 ->5->NULL

        pbefore:dummy
        m-1(1)个循环之后
        pbefore:1

        tail:pbefore.next(2)

        pre, p = None, 2
        n-m(2)个循环之后
        2->None, pre, p = 2, 3
        3->2,    pre, p = 3, 4

        
        2.next = 5
        1.next = 4
        4.next = 3
        dummy->1->4->3->2->5->NULL
        return dummy.next


        """
        if m == n:
            return head
        
        dummy = ListNode(-1)
        dummy.next = head

        pbefore = dummy
        for _ in range(m-1):
            pbefore = pbefore.next
        
        pre, p = None, pbefore.next
        # tail为反转开始的节点，经过反转变为尾节点
        tail = pbefore.next
        for _ in range(n-m):
            tmp = p.next
            p.next = pre
            pre = p
            p = tmp
        tail.next = p.next
        pbefore.next = p
        p.next = pre

        # 如果m=1，那么dummy.next将不再是head
        # 此时，dummy和pbefore指向相同，在第34行dummy.next改变了
        return dummy.next

        


        

