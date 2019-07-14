#
# @lc app=leetcode.cn id=154 lang=python3
#
# [154] 寻找旋转排序数组中的最小值 II
# https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/solution/154-find-minimum-in-rotated-sorted-array-ii-by-jyd/
#
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l, r = 0, len(nums)-1
        while l <= r:
            mid = l + ((r - l ) >> 1)
            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] < nums[r]:
                r = mid
            else:
                r -= 1
        return nums[l]

