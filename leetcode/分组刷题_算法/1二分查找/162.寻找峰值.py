#
# @lc app=leetcode.cn id=162 lang=python3
#
# [162] 寻找峰值
#
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            if l == r:
                return l
            mid = l + ((r - l) >> 1)
            if nums[mid] < nums[mid+1]:
                l = mid + 1
            else:
                r = mid

