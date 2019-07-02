'''
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]
'''

# 思路：

# 二分法，先找target出现的左边界，判断是否有target后再判断右边界

# 找左边界：二分，找到一个index
# 该index对应的值为target
# 并且它左边index-1对应的值不是target（如果index为0则不需要判断此条件）
# 如果存在index就将其append到res中
# 判断此时res是否为空，如果为空，说明压根不存在target，返回[-1, -1]
# 找右边界：二分，找到一个index（但是此时用于二分循环的l可以保持不变，r重置为len(nums)-1，这样程序可以更快一些）
# 该index对应的值为target
# 并且它右边index+1对应的值不是target（如果index为len(nums)-1则不需要判断此条件）
# 如果存在index就将其append到res中

class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1,-1]
        res = []
        l,r = 0,len(nums)-1
        #表面三种情况，其实是四种情况，
        #第四种情况是nums[mid] == target为真，(mid==0 or nums[mid-1]!=target)为假
        #这种情况下需要找的区间开头应该在mid左边，所以同样是把r = mid - 1
        while l<=r:
            mid = l+((r-l) >> 1)
            if nums[mid] == target and (mid==0 or nums[mid-1]!=target):
                res.append(mid)
                break
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
                
        if not res:
            return [-1, -1]
        
        r = len(nums)-1
        while l<=r:
            mid = l+((r-l) >> 1)
            if nums[mid] == target and (mid==len(nums)-1 or nums[mid+1]!=target):
                res.append(mid)
                break
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
                
        return res
