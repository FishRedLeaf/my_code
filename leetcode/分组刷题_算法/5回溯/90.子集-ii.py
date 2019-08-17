#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#
class Solution:
    # 89.84%
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]
        temp_size = 0
        for i in range(len(nums)):
            start = temp_size if i >= 1 and nums[i] == nums[i-1] else 0
            temp_size = len(res)
            for j in range(start, temp_size):
                res.append(res[j]+[nums[i]])
        return res

    # 回溯去重 24%
    # def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    #     self.ans = []
    #     def backtrack(nums, index, path):
    #         if index == len(nums):
    #             if sorted(path) not in self.ans:
    #                 self.ans.append(sorted(path))
    #             return
    #         backtrack(nums, index+1, path)
    #         backtrack(nums, index+1, path+[nums[index]])
    #     backtrack(nums, 0, [])
    #     return self.ans

