#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个有序数组的中位数
# http://chaoren.is-programmer.com/posts/42890.html
#
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        l1, l2 = len(nums1), len(nums2)
        if (l1 + l2) % 2 == 1:
            return 1.0  * self.getMedian(nums1, nums2, (l1 + l2) // 2 + 1)
        else:
            return 0.5 * (self.getMedian(nums1, nums2, (l1+l2)//2) + self.getMedian(nums1, nums2, (l1+l2)//2+1))

        
    def getMedian(self, A, B, k):
        # return kth smallest number of arrays A and B, assume len(A) <= len(B)
        la, lb = len(A), len(B)
        if la > lb:
            return self.getMedian(B, A, k)
        if la == 0:
            return B[k-1]
        if k == 1:
            return min(A[0], B[0])
        pa = min(k//2, la)
        pb = k - pa
        return self.getMedian(A[pa:], B, k-pa) if A[pa-1] <= B[pb-1] else self.getMedian(A, B[pb:], k-pb)

