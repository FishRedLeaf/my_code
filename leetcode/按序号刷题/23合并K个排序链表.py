# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 11:29:18 2019

@author: 鱼红叶

合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

import heapq
class Solution:
    def mergeKLists(self, lists):
        heap = []
        for list_head in lists:
            if list_head:
                heapq.heappush(heap, (list_head.val, list_head))
        p = ListNode(-1)
        dummy = p
        while heap:
            min_node = heapq.heappop(heap)[1]
            p.next = min_node
            p = p.next
            if min_node.next:
                heapq.heappush(heap, (min_node.next.val, min_node.next))
        return dummy.next