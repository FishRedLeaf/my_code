#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#
class Solution:
    # 双指针
    def sortColors(self, nums: List[int]) -> None:
        zero_idx, two_idx = 0, len(nums)-1
        i = 0
        while i <= two_idx:
            if nums[i] == 0:
                nums[zero_idx], nums[i] = nums[i], nums[zero_idx]
                zero_idx += 1
                i += 1
            elif nums[i] == 2:
                nums[two_idx], nums[i] = nums[i], nums[two_idx]
                two_idx -= 1
            else:
                i += 1


    # # 计数排序
    # def sortColors(self, nums: List[int]) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     d = {}
    #     for n in nums:
    #         d[n] = d.get(n, 0) + 1
    #     a, b, c = (d.get(i, 0) for i in (0,1,2))
    #     nums[:a] = [0] * a
    #     nums[a:a+b] = [1] * b
    #     nums[a+b:] = [2] * c

