class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        left, right = 0, len(nums) - 1
        res = []
        while left <= right:
            mid = left + ((right - left) >> 1)
            if nums[mid] == target and (mid == 0 or nums[mid] != nums[mid-1]):
                res.append(mid)
                break
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if not res:
            return [-1, -1]
        right = len(nums) - 1
        while left <= right:
            mid = left + ((right - left) >> 1)
            if nums[mid] == target and (mid == len(nums) - 1 or nums[mid] != nums[mid+1]):
                res.append(mid)
                break
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return res