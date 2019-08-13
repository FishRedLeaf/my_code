# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 18:05:01 2019

@author: 鱼红叶

参考https://blog.csdn.net/weixin_33862514/article/details/86015472
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
# 大于left->val放到右边，小于left->val放到左边
def partition(left, right):
    pv = left.val
    i, j = left, left.next
    while j != right:
        if j.val < pv:
            i = i.next
            i.val, j.val = j.val, i.val
        j = j.next
    left.val, i.val = i.val, left.val
    return i

def quick_sort(left, right):
    if left != right:
        mid = partition(left, right)
        quick_sort(left, mid)
        quick_sort(mid.next, right)
        
def create(items):
    head = ListNode(items[0])
    p = head
    for i in items[1:]:
        p.next = ListNode(i)
        p = p.next
    return head

def print_nodes(head):
    while head:
        print(head.val, end=' ')
        head = head.next
    
head = create([4,2,5,3,7,9,0,1])
quick_sort(head, None)
print_nodes(head)

