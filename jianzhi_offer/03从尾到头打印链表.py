# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 13:05:22 2019

@author: 鱼红叶

输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        res = []
        while listNode:
            res.append(listNode.val)
            listNode = listNode.next
        res.reverse()
        return res
        