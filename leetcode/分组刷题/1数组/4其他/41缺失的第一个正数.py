# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 22:24:07 2019

@author: 鱼红叶
"""

class Solution:
    def firstMissingPositive(self, nums):
        k = len(nums)
        if k == 0:
            return 1
        
        for i in range(k):
            while 0 < nums[i] <= k and nums[i] != nums[nums[i]-1]:
#                print(nums[i], nums[nums[i]-1])
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
                print(nums)
        for i in range(k):
            if nums[i] != i+1:
                return i+1
        return k+1
    
    def firstMissingPositive2(self, nums):
        '''
        哈希 key:数字，value:该数字作为索引，对应位置数的正负，正表示有，负表示没有
        1.检查 1 是否存在于数组中。如果没有，则已经完成，1 即为答案。
        2.如果 nums = [1]，答案即为 2 。
        3.将负数，零，和大于 n 的数替换为 1 。
        4.遍历数组。当读到数字 a 时，替换第 a 个元素的符号。 
        注意重复元素：只能改变一次符号。由于没有下标 n ，
        使用下标 0 的元素保存是否存在数字 n。
        5.再次遍历数组。返回第一个正数元素的下标。
        6.如果 nums[0] > 0，则返回 n 。
        7.如果之前的步骤中没有发现 nums 中有正数元素，则返回n + 1。
        '''
        n = len(nums)
        if 1 not in nums:
            return 1
        if n == 1:
            return 2
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1
        for i in range(n):
            a = abs(nums[i])
            if a == n:
                nums[0] = -abs(nums[0])
            else:
                nums[a] = -abs(nums[a])
        for i in range(1, n):
            if nums[i] > 0:
                return i
        if nums[0] > 0:
            return n
        return n+1
    
print(Solution().firstMissingPositive2([1,3,-1,5,2]))