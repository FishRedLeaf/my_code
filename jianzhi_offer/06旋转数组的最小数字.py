# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 15:30:49 2019

@author: 鱼红叶

把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 
输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。 
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
"""


class Solution:
    #O(n)
    def minNumberInRotateArray(self, rotateArray):
        for i in range(1, len(rotateArray)):
            if rotateArray[i] < rotateArray[i-1]:
                return rotateArray[i]

    #O(logn)
    def minNumberInRotateArray2(self, rotateArray):
        l = len(rotateArray)
        if l == 0:
            return 0
        if l == 1:
            return rotateArray[0]
        left, right = 0, l-1
        while left <= right:
            mid = left + (right-left) // 2
            if rotateArray[mid] > rotateArray[right]:
                left = mid + 1
            elif rotateArray[mid] < rotateArray[right]:
                right = mid
            else:
                right -= 1
        return rotateArray[left]
                