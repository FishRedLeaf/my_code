class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        i = 0
        res = sum(nums[:3])
        min_abs = abs(res - target)
        while i <= len(nums) - 3:
            left, right = i + 1, len(nums) - 1
            while left < right:
                val = nums[i] + nums[left] + nums[right]
                if val == target:
                    return val
                elif val < target:
                    if abs(val - target) < min_abs:
                        min_abs = min(min_abs, abs(val - target))
                        res = val
                    left += 1
                else:
                    if abs(val - target) < min_abs:
                        min_abs = min(min_abs, abs(val - target))
                        res = val
                    right -= 1
            i += 1
        return res