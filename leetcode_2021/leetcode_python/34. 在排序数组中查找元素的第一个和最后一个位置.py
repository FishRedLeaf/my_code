
# while left <= right
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

# while left < right 正常都是<=，仅有找边界的情况使用<
# < 对应左闭右开 left, right = 0, len(nums)
# <= 对应左闭右开 left, right = 0, len(nums) - 1
class Solution2:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        """
        # 在[left, right)中找最左边索引
        # 如果nums[mid]=target，则new_right=mid
        # 这样在[left, new_right)中找最左边索引，
        # 若这个区间不存在target,则返回mid
        """
        res = []
        left, right = 0, len(nums)
        while left < right:
            mid = left + ((right - left) >> 1)
            if nums[mid] == target:
                right = mid
            elif nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
        if left == len(nums) or nums[left] != target:
            return [-1, -1]
        res.append(left)

        right = len(nums)
        while left < right:
            mid = left + ((right - left) >> 1)
            if nums[mid] == target and left != mid:
                left = mid
            elif nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                left = mid + 1
        if left == len(nums) or nums[left] != target:
            res.append(left-1)
        else:
            res.append(left)
        return res

# Solution2是经过调试所得，Solution3是(while left < right)的标准写法
class Solution3:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        """
        # 在[left, right)中找最左边索引
        # 如果nums[mid]=target，则new_right=mid
        # 这样在[left, new_right)中找最左边索引，
        # 若这个区间不存在target,则返回mid
        """
        res = []
        left, right = 0, len(nums)
        while left < right:
            mid = left + ((right - left) >> 1)
            if nums[mid] == target:
                right = mid
            elif nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
        if left == len(nums) or nums[left] != target:
            return [-1, -1]
        res.append(left)

        right = len(nums)
        while left < right:
            mid = left + ((right - left) >> 1)
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
        if left == 0 or nums[left-1] != target:
            return [-1, -1]
        res.append(left-1)
        return res

