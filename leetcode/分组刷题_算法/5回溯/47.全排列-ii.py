#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#
class Solution:
    def permuteUnique(self, nums):
        self.res = []
        nums.sort()
        L = len(nums)
        def dfs(nums, path, visited):
            if len(path) == L:
                self.res.append(path)
                return
            for i, n in enumerate(nums):
                if i in visited:
                    continue
                # [1,2,2,3]保证第一个1和第二个1加进visited的先后顺序
                if i > 0 and nums[i-1] == n and i-1 not in visited:
                    continue
                visited.add(i)
                dfs(nums, path+[n], visited)
                visited.remove(i)
        dfs(nums, [], set())
        return self.res

# print(Solution().permuteUnique([1,1,2]))
