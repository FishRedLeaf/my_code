
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        pFast, pSlow = head, head
        while pFast and pFast.next:
            pFast = pFast.next.next
            pSlow = pSlow.next
            if pSlow == pFast:
                return True
        return False