'''
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？
找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

class Solution:
    def threeSum(self, nums):
        nums.sort()
        res = []
        for i in range(len(nums)):
            #[1,1,2,3,……] i=0时,考虑过nums[j]=1,2,3的情况，不必再考虑i=1时nums[j]=2,3的情况了
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

nums = [-1, 0, 1, 2, -1, -4]
print(Solution().threeSum(nums))