# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 18:05:20 2019

@author: 鱼红叶
"""

from heapq import heappush, heappop

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
h = []

heappush(h, (5, ListNode(5)))
heappush(h, (7, ListNode(7)))
heappush(h, (1, ListNode(1)))
heappush(h, (3, ListNode(3)))
print(heappop(h))
