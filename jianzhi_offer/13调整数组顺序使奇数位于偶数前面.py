# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 21:25:50 2019

@author: 鱼红叶

输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，
并保证奇数和奇数，偶数和偶数之间的相对位置不变。
"""

class Solution:
    def reOrderArray(self, array):
        left, right = [], []
        for a in array:
            if a % 2 == 0:
                right.append(a)
            else:
                left.append(a)
        return left+right
    
    def reOrderArray2(self, array):
        #不使用额外空间,不能保证相对位置不变
        p1, p2 = 0, len(array)-1
        while p1 != p2:
            if array[p1] % 2 == 1:
                p1 +=1
                continue
            if array[p2] % 2 == 0:
                p2 -= 1
                continue
            if array[p1]%2 == 0 and array[p2]%2 == 1:
                array[p1],array[p2] = array[p2],array[p1]
                p1 += 1
                p2 -= 1
        return array
    
    def reOrderArray3(self, array):
        #类似冒泡排序的做法
        for i in range(len(array)):
            for j in range(len(array)-1,i,-1):
                if array[j]%2 == 1 and array[j-1]%2 == 0:
                    array[j],array[j-1] = array[j-1],array[j]
        return array

print(Solution().reOrderArray3([1,2,3,4,5]))   