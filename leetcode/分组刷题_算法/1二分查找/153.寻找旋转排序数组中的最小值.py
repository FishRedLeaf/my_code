#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#
# 93.7
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l, r = 0, len(nums)-1
        while l <= r:
            mid = l + ((r - l) >> 1)
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid-1] > nums[mid]:
                return nums[mid]
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

