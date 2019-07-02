'''
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        mid = self.mid(head)
        p1 = head
        p2 = self.reverse(mid)
        while p1 and p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True
    
    def mid(self, head):
        pSlow, pFast = head, head
        while pFast and pFast.next:
            pFast = pFast.next.next
            pSlow = pSlow.next
        return pSlow
    
    def reverse(self, head):
        p1, p2 = head, None
        while p1:
            tmp = p1.next
            p1.next = p2
            p2 = p1
            p1 = tmp
        return p2