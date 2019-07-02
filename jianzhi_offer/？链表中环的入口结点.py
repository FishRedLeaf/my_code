# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 16:01:38 2019

@author: 鱼红叶

给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def EntryNodeOfLoop(self, pHead):
        meetingNode = self.MeetingNode(pHead)
        if not meetingNode:
            return None
        
        lenCircle = 1
        p1 = meetingNode
        while p1.next != meetingNode:
            p1 = p1.next
            lenCircle += 1
            
        p1 = pHead
        for _ in range(lenCircle):
            p1 = p1.next
        p2 = pHead
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1
        
    def MeetingNode(self, pHead):
        if not pHead:
            return None
        pSlow = pHead.next
        if not pSlow:
            return None
        pFast = pSlow.next
        
        while pSlow and pFast:
            if pSlow == pFast:
                return pFast
            pSlow = pSlow.next
            pFast = pFast.next
            if pFast:
                pFast = pFast.next
        return None
            
        