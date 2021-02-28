class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums
        i = len(nums) - 1
        while i >= 1 and nums[i] <= nums[i-1]:
            i -= 1
        if i == 0:
            nums.sort()
        left = i - 1
        i = len(nums) - 1
        while i >= left + 1 and nums[i] <= nums[left]:
            i -= 1
        nums[left], nums[i] = nums[i], nums[left]
        nums[left+1:] = sorted(nums[left+1:])
        
            