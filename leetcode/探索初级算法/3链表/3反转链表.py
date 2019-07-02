'''
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    #迭代
    def reverseList(self, head: ListNode) -> ListNode:
        p1, p2 = head, None
        while p1:
            tmp = p1.next
            p1.next = p2
            p2 = p1
            p1 = tmp
        return p2
    #递归
    def reverseList2(self, root: ListNode) -> ListNode:
        if not root or not root.next:
            return root
        res = self.reverseList(root.next)
        root.next.next = root
        root.next = None
        return res