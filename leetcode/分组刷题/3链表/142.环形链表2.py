# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
三种解法
set 使用额外空间较大
来自剑指offer 步骤较多
Floyd 需要证明
'''
# class Solution(object):
#     def detectCycle(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         visited = set()
#         p = head
#         while p:
#             if p in visited:
#                 return p
#             else:
#                 visited.add(p)
#                 p = p.next
#         return None

# class Solution(object):
#     def detectCycle(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         if not head:
#             return None
        
#         def hasCycle(head):
#             slow, fast = head, head
#             while fast and fast.next:
#                 slow = slow.next
#                 fast = fast.next.next
#                 if slow == fast:
#                     return slow
#             return None
#         meetingNode = hasCycle(head)
#         if not meetingNode:
#             return None
#         p = meetingNode.next
#         c = 1
#         while p != meetingNode:
#             p = p.next
#             c += 1

#         p1, p2 = head, head
#         for _ in range(c):
#             p1 = p1.next
#         while p1 != p2:
#             p1 = p1.next
#             p2 = p2.next
#         return p1

# Floyd算法
# https://leetcode-cn.com/problems/linked-list-cycle-ii/solution/huan-xing-lian-biao-ii-by-leetcode/
# head到环入口节点距离L，入口节点到meetingNode距离a，meetingNode节点到入口节点距离b
# p1, p2 = head, meetingNode
# 最终相遇在环入口节点时，各自走的距离为
# L+k1*(a+b), k2(a+b)+b
# 相遇时距离head 的距离分别为
# L+k1*(a+b), L+a + k2*(a+b)+b = L+(k2+1)*(a+b)
# 都是在环的入口节点上(即 L + 整数倍 * (a+b))

# 注意各自走的距离L+k1*(a+b) = k2(a+b)+b
# meetingNode: 快慢指针 2 * (L+a) = L + n * (a+b) + a => L = (n-1)*(a+b) + b
# 因此只要满足k2-k1 = n-1即可

class Solution(object):
    def detectCycle(self, head):
        if not head:
            return None
        
        def hasCycle(head):
            slow, fast = head, head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    return slow
            return None
        meetingNode = hasCycle(head)
        if not meetingNode:
            return None
        p1, p2 = head, meetingNode
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1