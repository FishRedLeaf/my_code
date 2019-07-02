'''
峰值元素是指其值大于左右相邻值的元素。

给定一个输入数组 nums，其中 nums[i] ≠ nums[i+1]，找到峰值元素并返回其索引。

数组可能包含多个峰值，在这种情况下，返回任何一个峰值所在位置即可。

你可以假设 nums[-1] = nums[n] = -∞。

示例 1:

输入: nums = [1,2,3,1]
输出: 2
解释: 3 是峰值元素，你的函数应该返回其索引 2。
示例 2:

输入: nums = [1,2,1,3,5,6,4]
输出: 1 或 5 
解释: 你的函数可以返回索引 1，其峰值元素为 2；
     或者返回索引 5， 其峰值元素为 6。
说明:

你的解法应该是 O(logN) 时间复杂度的。
'''

#仅能在python2通过
class Solution:
    def findPeakElement(self, nums) -> int:
        start, end = 0, len(nums)-1
        while start+1 < end:
            mid = start + (end - start) // 2
            if nums[mid] < nums[mid+1]:
                start = mid
            else:
                end = mid
        if nums[start] > nums[end]:
            return start
        return end

#在python3也能通过
class Solution2(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            if l == r : return l
            mid = l + ((r - l) >> 2)
            if nums[mid] < nums[mid+1]:
                l = mid + 1
            else:
                r = mid
print(Solution2().findPeakElement([1,2]))
            