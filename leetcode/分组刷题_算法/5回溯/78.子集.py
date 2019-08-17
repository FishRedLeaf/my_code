#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#
class Solution:

    # 回溯标准写法
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        def backtrack(nums, index, path):
            if index == len(nums):
                self.ans.append(path)
                return
            backtrack(nums, index+1, path)
            backtrack(nums, index+1, path+[nums[index]])
        backtrack(nums, 0, [])
        return self.ans

    # dfs
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     self.ans = []
    #     def dfs(nums, index, path):
    #         self.ans.append(path)
    #         for i in range(index, len(nums)):
    #             dfs(nums, i+1, path+[nums[i]])
    #     dfs(nums, 0, [])
    #     return self.ans

    # 一种巧妙的方法
    # def subsets(self, nums):
    #     res = [[]]
    #     for i in range(len(nums)):
    #         for subres in res[:]: 
    #             res.append(subres+[nums[i]])
    #     return res

