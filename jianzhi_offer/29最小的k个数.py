# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 21:40:25 2019

@author: 鱼红叶

输入n个整数，找出其中最小的K个数。
例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
"""
class Solution:
    def GetLeastNumbers_Solution(self, nums, k):
        def quick_select(nums, start, end, k):
            if start == end:
                return nums[:start+1]
            mid = Partition(nums, start, end)
            if mid == k:
                return sorted(nums[:k+1])
            elif mid > k:
                return quick_select(nums, start, mid-1, k)
            else:
                return quick_select(nums, mid+1, end, k)

        def Partition(nums, start, end):
            import random
            p = random.randint(start, end)
            pv = nums[p]
            nums[p], nums[end] = nums[end], nums[p]
            mid = start
            for i in range(start, end):
                if nums[i] <= pv:
                    nums[i],nums[mid] = nums[mid],nums[i]
                    mid += 1
            nums[mid], nums[end] = nums[end], nums[mid]
            return mid
        return quick_select(nums, 0, len(nums)-1, k-1)
    
class Solution2:
    def GetLeastNumbers_Solution(self, nums, k):
        # write code here
        if nums == None or len(nums) < k or len(nums) <= 0 or k <= 0:
            return []
        
        n = len(nums)
        start, end = 0, n-1
        index = self.Partition(nums, n, start, end)
        while index != k-1:
            if index>k-1:
                end = index - 1
                index = self.Partition(nums,n,start,end)
            else:
                start = index + 1
                index = self.Partition(nums,n,start,end)
        output = nums[:k]
        output.sort()
        return output
    
    def Partition(self,nums,n,start,end):
        if nums==None or n<=0 or start<0 or end>n:
            return None
        if end == start:
            return end
        pivotvalue = nums[start]
        left = start+1
        right = end
         
        done = False
        while not done:
            while nums[left] <= pivotvalue and left<=right:
                left += 1
            while nums[right] >= pivotvalue and right>=left:
                right -= 1
            if left > right:
                done = True
            else:
                nums[left],nums[right] = nums[right],nums[left]
        nums[right],nums[start] = nums[start],nums[right]
        return right

        
print(Solution().GetLeastNumbers_Solution([4,5,1,6,2,7,3,8],8))