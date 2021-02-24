class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        if nums[0] > 0 or nums[-1] < 0:
            return []
        i = 0
        res = []
        # 遍历数组取元素1，在元素1右侧用双指针取元素2和元素3
        # 注意一定要先判断a+b+c=0，再判断重复，否则会丢失-2+1+1=0
        while i <= len(nums) - 3 and nums[i] <= 0:
            if i >= 1 and nums[i] == nums[i-1]:
                i += 1
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1
            i += 1
        return res