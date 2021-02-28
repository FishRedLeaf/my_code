class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 0
        while i <= len(nums) - 1:
            nums[j] = nums[i]
            while i <= len(nums) - 1 and nums[i] == nums[j]:
                i += 1
            j += 1
        return j