'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''

class Solution:
    def twoSum(self, nums, target):
        ddd = {}
        for i in range(len(nums)):
            if target-nums[i] in ddd:
                return [ddd[target-nums[i]], i]
            ddd[nums[i]] = i

    def twoSum2(self, nums, target):
        ddd = {}
        for i, n in enumerate(nums):
            if target-n in ddd:
                return [ddd[target-n], i]
            ddd[n] = i

print(Solution().twoSum2([2,7,11,15], 9))