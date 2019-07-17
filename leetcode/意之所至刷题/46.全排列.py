#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#
class Solution:

    # 89.5%
    def permute(self, nums: List[int]) -> List[List[int]]:

        def backtrack(first=0):
            if first == n:
                res.append(nums[:])
            else:
                for i in range(first, n):
                    nums[first], nums[i] = nums[i], nums[first]
                    backtrack(first+1)
                    nums[first], nums[i] = nums[i], nums[first] 
        
        n = len(nums)
        res = []
        backtrack()
        return res

    # # 89.5%
    # def permute(self, nums: List[int]) -> List[List[int]]:
    #     if not nums:
    #         return []
    #     if len(nums) == 1:
    #         return [nums]
    #     res = []
    #     for i in range(len(nums)):
    #         prefix = nums[i]
    #         rest = nums[:i] + nums[i+1:]
    #         for j in self.permute(rest):
    #             res.append([prefix] + j)
    #     return res

