#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个排序链表
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 86.99% python
# class Solution:
#     def mergeKLists(self, lists):
#         import heapq
#         heap = []
#         for list_head in lists:
#             if list_head:
#                 heapq.heappush(heap, ((list_head.val, list_head)))

#         p = ListNode(-1)
#         dummy = p
#         while heap:
#             min_node = heapq.heappop(heap)[1]
#             p.next = min_node
#             p = p.next
#             if min_node.next:
#                 heapq.heappush(heap, (min_node.next.val, min_node.next))
#         return dummy.next

# python3 9.89%
class Solution:
    def mergeKLists(self, lists):

        def heapify(unsorted, index, heap_size):
            largest = index
            left_index = 2 * index + 1
            right_index = 2 * index + 2
            if left_index < heap_size and unsorted[left_index][0] < unsorted[largest][0]:
                largest = left_index
            if right_index < heap_size and unsorted[right_index][0] < unsorted[largest][0]:
                largest = right_index

            if largest != index:
                unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
                heapify(unsorted, largest, heap_size)

        def heap_sort(unsorted):
            n = len(unsorted)
            for i in range(n // 2 - 1, -1, -1):
                heapify(unsorted, i, n)
            for i in range(n - 1, 0, -1):
                    unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
                    heapify(unsorted, 0, i)

        unsorted = []
        for list_head in lists:
            if list_head:
                unsorted.append((list_head.val, list_head))
        heap_sort(unsorted)

        p = ListNode(-1)
        dummy = p
        while unsorted:
            min_node = unsorted.pop()[1]
            p.next = min_node
            p = p.next
            if min_node.next:
                unsorted.append((min_node.next.val, min_node.next))
                heap_sort(unsorted)
        return dummy.next    

            
