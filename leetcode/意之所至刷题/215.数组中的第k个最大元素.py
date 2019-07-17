#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#
import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickselct(start, end, nums, k):
            if start == end:
                return nums[start]
            mid = partition(start, end, nums)
            if mid == k:
                return nums[mid]
            elif k > mid:
                return quickselct(mid+1, end, nums, k)
            else:
                return quickselct(start, mid-1, nums, k)

        def partition(start, end, nums):
            p = random.randint(start, end)
            pv = nums[p]
            nums[p], nums[end] = nums[end], nums[p]
            mid = start
            for i in range(start, end):
                if nums[i] >= pv:
                    nums[i], nums[mid] = nums[mid], nums[i]
                    mid += 1
            nums[mid], nums[end] = nums[end], nums[mid]
            return mid
            
        return quickselct(0, len(nums)-1, nums, k-1)
        

