#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#
import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 等价于找排序后索引为k-1的元素
        n = len(nums)
        return self.helper(nums, 0, n-1, k-1)
            
    def helper(self, nums, left, right, k):
        if left == right:
            return nums[left]
        # nums[mid]为第mid+1个最大元素
        mid = self.partition(nums, left, right)
        if mid == k:
            return nums[mid]
        elif k > mid:
            return self.helper(nums, mid+1, right, k)
        else:
            return self.helper(nums, left, mid-1, k)
        
    def partition(self, nums, left, right):
        p = random.randint(left, right)
        pv = nums[p]
        nums[p], nums[right] = nums[right], nums[p]
        mid = left
        for i in range(left, right):
            if nums[i] >= pv:
                nums[i], nums[mid] = nums[mid], nums[i]
                mid += 1
        nums[mid], nums[right] = nums[right], nums[mid]
        return mid

                

