class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for n in nums:
                if n not in path:
                    path.append(n)
                    backtrack(path)
                    path.pop()
            
        res = []
        backtrack([])
        return res