
# leetcode 链表类的题

# 2. 两数相加
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val + l2.val < 10:
            l3 = ListNode(l1.val+l2.val)
            l3.next = self.addTwoNumbers(l1.next, l2.next)
        else:
            l3 = ListNode(l1.val+l2.val-10)
            tmp = ListNode(1)
            l3.next = self.addTwoNumbers(self.addTwoNumbers(l1.next, tmp), l2.next)
        return l3

# 19. 删除链表的倒数第N个节点
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head

        p1, p2 = dummy, dummy
        for _ in range(n):
            p1 = p1.next

        while p1.next:
            p1 = p1.next
            p2 = p2.next
        p2.next = p2.next.next
        return dummy.next


# 21. 合并两个有序链表
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1

        dummy = ListNode(-1)
        p = dummy
        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        if l1:
            p.next = l1
        if l2:
            p.next = l2
        return dummy.next

# 23. 合并K个排序链表
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        import heapq
        heaplist = []
        for head in lists:
            if head:
                heaplist.append((head.val, head))
        heapq.heapify(heaplist)

        dummy = ListNode(-1)
        p = dummy
        while heaplist:
            val, node = heapq.heappop(heaplist)
            p.next = node
            p = p.next
            if node.next:
                heapq.heappush(heaplist, (node.next.val, node.next))

        return dummy.next

# 24. 两两交换链表中的节点
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        p1, p2 = head, head.next
        while p2:
            tmp = p2.next
            p2.next = p1
            pre.next = p2
            p1.next = tmp
            pre = p1
            p1 = p1.next
            if not p1:
                break
            p2 = p1.next

        return dummy.next

# 206. 反转链表
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        pre, p = None, head
        while p:
            tmp = p.next
            p.next = pre
            pre = p
            p = tmp
        return pre

# 92. 反转链表 II
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head
        dummy = ListNode(-1)
        dummy.next = head

        front = dummy
        for _ in range(m-1):
            front = front.next
        pre, p = front, front.next
        tail = p

        for _ in range(n-m):
            tmp = p.next
            p.next = pre
            pre = p
            p = tmp
        front.next = p
        tail.next = p.next
        p.next = pre
        return dummy.next

# 25. K 个一组翻转链表
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:




# 109. 有序链表转换二叉搜索树
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)

        pre = None
        slow, fast = head, head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        if pre:
            pre.next = None

        root = TreeNode(slow.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)
        return root

# 108. 将有序数组转换为二叉搜索树
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        mid = len(nums) // 2
        head = TreeNode(nums[mid])
        head.left = self.sortedArrayToBST(nums[:mid])
        head.right = self.sortedArrayToBST(nums[mid+1:])
        return head