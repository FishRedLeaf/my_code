class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        nums.sort()
        i = 0
        res = []
        while i <= len(nums) - 4:
            if i >= 1 and nums[i] == nums[i-1]:
                i += 1
                continue
            j = i + 1
            while j <= len(nums) - 3:
                if j >= i + 2 and nums[j] == nums[j-1]:
                    j += 1
                    continue
                left, right = j + 1, len(nums) - 1
                while left < right:
                    if nums[i] + nums[j] + nums[left] + nums[right] == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1
                    elif nums[i] + nums[j] + nums[left] + nums[right] < target:
                        left += 1
                    else:
                        right -= 1
                j += 1
            i += 1
        return res