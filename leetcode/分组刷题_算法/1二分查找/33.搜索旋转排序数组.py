#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#
class Solution:
    def search(self, nums, target):
        if not nums:
            return -1

        l, r = 0, len(nums)-1
        while l <= r:
            mid = l + ((r - l ) >> 1)
            # print(mid)
            if nums[mid] == target:
                return mid
            # 左边是有序的, 注意数组长度为2时，mid=l,
            # l和mid重合时，跟nums[l] < nums[mid]归为一类
            # 因为nums[mid]!=target,所以nums[l]!=target,
            # 所以l_new = mid + 1
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
# print(Solution().search([5,1,2,3,4], 1))

