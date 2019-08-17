#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#
class Solution:
    # 基于回溯算法98.84%
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        L = len(nums)
        def dfs(nums, path, visited):
            if len(path) == L:
                self.res.append(path)
                return
            for n in nums:
                if n not in visited:
                    visited.add(n)
                    dfs(nums, path+[n], visited)
                    visited.remove(n)
        dfs(nums, [], set())
        return self.res
        

    # 14.59%
    # def permute(self, nums: List[int]) -> List[List[int]]:
    #     if not nums:
    #         return []
    #     if len(nums) == 1:
    #         return [nums]
    #     res = []
    #     for i, n in enumerate(nums):
    #         rest = nums[:i] + nums[i+1:]
    #         for a in self.permute(rest):
    #             res.append([n] + a)
    #     return res

