'''
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
'''
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #i表示原始数组的索引,j表示新数组的索引
        i, j, l = 1, 0, len(nums)-1
        while i <= l:
            if nums[i] != nums[j]:
                nums[j+1] = nums[i]
                j += 1
            i += 1
        return j+1
          
nums = [0,1,1,2,2,2,3,3]
l = Solution().removeDuplicates(nums)
for i in range(l):
    print(nums[i])