class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def backtrack(path, visited):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i, n in enumerate(nums):
                if i in visited:
                    continue
                # 如果nums[i]=nums[i-1]，那么限制一定要nums[i-1]在nums[i]前面
                # 因为nums[i-1],xxx,nums[i]和nums[i],xxx,nums[i-1]是重复的
                if i > 0 and (nums[i-1] == n and i-1 not in visited):
                    continue
                visited.add(i)
                backtrack(path+[n], visited)
                visited.remove(i)
        res = []
        backtrack([], set())
        return res
                

# 非全排列，完全去重的写法
# class Solution2:
#     def permuteUnique(self, nums: List[int]) -> List[List[int]]:
#         unique_idx = [0]
#         for i in range(1, len(nums)):
#             if nums[i] != nums[i-1]:
#                 unique_idx.append(i)
#         unique_idx.append(len(nums))
#         def backtrack(path):
#             if len(path) == len(nums):
#                 res.append(path[:])
#                 return
#             for i in range(len(unique_idx)-1):
#                 index = unique_idx[i]
#                 if nums[index] not in path:
#                     path.extend([nums[index]] * (unique_idx[i+1] - index))
#                     backtrack(path)
#                     path = path[:len(path)-(unique_idx[i+1] - index)]
#         res = []
#         backtrack([])
#         return res
                