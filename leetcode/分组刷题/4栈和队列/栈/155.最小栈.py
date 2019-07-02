#
# @lc app=leetcode.cn id=155 lang=python
#
# [155] 最小栈
#
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_ = None
        
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if self.min_ == None or self.min_ > x:
            self.min_ = x

    def pop(self):
        """
        :rtype: None
        """
        popItem = self.stack.pop()
        if len(self.stack) == 0:
            self.min_ = None
        if popItem == self.min_:
            self.min_ = min(self.stack)

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

