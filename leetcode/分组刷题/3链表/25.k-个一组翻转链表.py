#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        p = head
        c = 0
        while p:
            p = p.next
            c += 1
        n = c // k
#        print('n:', n)
        if n == 0 or k == 1:
            return head
        
        pbefore = ListNode(-1)
        pbefore.next = head
        pre, p = None, head
        tail = head
        
#        print(p.val, tail.val)
        for i in range(n):
            # 反转(i-1)*k+1 ~ i*k之间的链表
            for _ in range(k-1):
                tmp = p.next
                p.next = pre
                pre = p
                p = tmp
#            print('p:', p.val)
            
            tail.next = p.next
            pbefore.next = p
            if i == 0:
                ret = pbefore.next
            p.next = pre
            
            pbefore = tail
            pre, p = None, tail.next
            tail = tail.next
#            print(p.val, tail.val)
#            print('process: ', end=' ')
#            print_nodes(ret)
        return ret

# def create(items):
#     head = ListNode(items[0])
#     p = head
#     for i in items[1:]:
#         p.next = ListNode(i)
#         p = p.next
#     return head

# def print_nodes(head):
#     while head:
#         print(head.val, end=' ')
#         head = head.next
#     print()
        
# head = create([1,2,3,4,5])
# print_nodes(head)
# head = Solution().reverseKGroup(head, 1)
# print_nodes(head)     









