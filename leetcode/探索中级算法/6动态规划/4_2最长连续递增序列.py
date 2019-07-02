'''
给定一个未经排序的整数数组，找到最长且连续的的递增序列。

示例 1:

输入: [1,3,5,4,7]
输出: 3
解释: 最长连续递增序列是 [1,3,5], 长度为3。
尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，因为5和7在原数组里被4隔开。 
示例 2:

输入: [2,2,2,2,2]
输出: 1
解释: 最长连续递增序列是 [2], 长度为1。
注意：数组长度不会超过10000。
'''
class Solution:
    def findLengthOfLCIS(self, nums) -> int:
        if not nums:
            return 0
        max_ = 0
        sublen = 1
        i = 0
        while i < len(nums)-1:
            if nums[i] < nums[i+1]:
                sublen += 1
            else:
                max_ = max(max_, sublen)
                sublen = 1
            i += 1
        
        return max(max_, sublen)

    #纯暴力
    def findLengthOfLCIS2(self, nums) -> int:
        if len(nums) <= 0: return 0
        if len(nums) == 1: return 1
        res = 1
        maxl = 1
        i = 1
        while i <= len(nums)-1:
            while i <= len(nums)-1 and nums[i] > nums[i-1]:
                maxl += 1
                i += 1
            res = max(res, maxl)
            maxl = 1
            i += 1
        return res
    
    def findLengthOfLCIS3(self, nums) -> int:
        res = 0
        count = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                count += 1
            else:
                res = max(count, res)
                count = 1
        return res

print(Solution().findLengthOfLCIS3([10,9,2,5,3,7,101,18]))