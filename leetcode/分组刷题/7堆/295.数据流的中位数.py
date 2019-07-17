#
# @lc app=leetcode.cn id=295 lang=python3
#
# [295] 数据流的中位数
#

import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.left = []
        self.right = []
        self.median = None

    def addNum(self, num: int) -> None:
        if self.median is None:
            self.median = num
            return 
        left, right = self.left, self.right
        if num <= self.median:
            heapq.heappush(left, -num)
        else:
            heapq.heappush(right, num)
        if len(left) > len(right) + 1:
            top = -heapq.heappop(left)
            heapq.heappush(right, self.median)
            self.median = top
        if len(right) > len(left) + 1:
            top = heapq.heappop(right)
            heapq.heappush(left, -self.median)
            self.median = top

    def findMedian(self) -> float:
        left, right = self.left, self.right
        if len(left) == len(right):
            return 1. * self.median
        elif len(left) > len(right):
            return 1. * (self.median - left[0]) / 2
        else:
            return 1. * (self.median + right[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

