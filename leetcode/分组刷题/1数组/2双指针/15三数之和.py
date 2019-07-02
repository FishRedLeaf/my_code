# -*- coding: utf-8 -*-
"""
Created on Mon May 27 21:16:23 2019

@author: 鱼红叶

给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，
使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
"""

class Solution:
    def threeSum(self, nums):
        '''
        双指针法
        首先数组排序
        遍历数组，当前遍历到的值设为a，固定了三个数中的a，
        接着一个指针指向a的下一个元素，一个指针指向数组的最后一个元素，
        三数之和大于0则右指针减1，否则左指针加1，等于0就加入结果集合中
        '''
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1

            while l < r:
                if nums[i]+nums[l]+nums[r] == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif nums[i]+nums[l]+nums[r] > 0:
                    r -= 1
                else:
                    l += 1
        return res
    
print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))