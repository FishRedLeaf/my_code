'''
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''
#本题机智解法
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for n in nums:
            res.extend([r+[n] for r in res])
        return res

#dfs
class Solution2(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(nums, idx, path, res):
            res.append(path)
            for i in range(idx, len(nums)):
                dfs(nums, i+1, path+[nums[i]], res)
        
        res = []
        dfs(nums, 0, [], res)
        return res

#标准回溯
class Solution3(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        self.backtrack(nums, [], 0)
        return self.res

    def backtrack(self, nums, path, idx):
        if len(nums) == idx:
            self.res.append(path)
            return
        self.backtrack(nums, path+[nums[idx]], idx+1)
        self.backtrack(nums, path, idx+1)
        
print(Solution3().subsets([1,2,3]))


        
            