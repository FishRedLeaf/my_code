'''
给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。

说明:

初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
示例:

输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]
'''

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            for i in range(len(nums1)):
                nums1[i] = nums2[i]
            # nums1 = nums2
        elif n == 0:
            return
        else:
            p1, p2, p = m-1, n-1, m+n-1
            while p1 >= 0 and p2 >= 0:
                if nums1[p1] > nums2[p2]:
                    nums1[p] = nums1[p1]
                    p1 -= 1
                else:
                    nums1[p] = nums2[p2]
                    p2 -= 1
                p -= 1
            #p1先到0，要把nums2中剩下的往里面扔；p2先到0，啥都不用干。
            while p2 != -1:
                nums1[p] = nums2[p2]
                p -= 1; p2 -= 1