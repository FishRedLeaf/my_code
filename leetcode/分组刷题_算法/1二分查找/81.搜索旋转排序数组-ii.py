#
# @lc app=leetcode.cn id=81 lang=python3
#
# [81] 搜索旋转排序数组 II

#https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii/solution/er-fen-by-powcai/
#
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = l + ((r - l) >> 1)
            if nums[mid] == target:
                return True
            if nums[mid] == nums[l] == nums[r]:
                r -= 1
                l += 1
            elif nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False
            

