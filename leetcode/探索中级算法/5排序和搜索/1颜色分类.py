'''
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

注意:
不能使用代码库中的排序函数来解决这道题。

示例:

输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]
进阶：

一个直观的解决方案是使用计数排序的两趟扫描算法。
首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
你能想出一个仅使用常数空间的一趟扫描算法吗？
'''

class Solution(object):
    def sortColors(self, nums):
        zero_idx, two_idx = 0, len(nums)-1
        i = 0
        while i <= two_idx:
            if nums[i] == 0:
                nums[i], nums[zero_idx] = nums[zero_idx], nums[i]
                zero_idx += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[two_idx] = nums[two_idx], nums[i]
                two_idx -= 1
            else:
                i += 1

    def sortColors2(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        c1,c2,c3 = 0,0,0
        for n in nums:
            if n == 0:
                c1 += 1
            if n == 1:
                c2 += 1
            if n == 2:
                c3 += 1
        c2 += c1
        c3 += c2
        for i in range(c1):
            nums[i] = 0
        for i in range(c1, c2):
            nums[i] = 1
        for i in range(c2, c3):
            nums[i] = 2

nums = [1,2,0] #[2,0,2,1,1,0]
Solution().sortColors(nums)
print(nums)