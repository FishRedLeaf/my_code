'''
给定两个数组，编写一个函数来计算它们的交集。

示例 1:

输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2,2]
示例 2:

输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [4,9]
说明：

输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
我们可以不考虑输出结果的顺序。
进阶:

如果给定的数组已经排好序呢？你将如何优化你的算法？
如果 nums1 的大小比 nums2 小很多，哪种方法更优？
如果 nums2 的元素存储在磁盘上，磁盘内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？
'''

class Solution:
    def intersect(self, nums1, nums2):
        d1, d2 = dict(), dict()
        for n in nums1:
            d1[n] = d1.get(n, 0) + 1
        for n in nums2:
            d2[n] = d2.get(n, 0) + 1
        
        keys = set(list(d1.keys())) & set(list(d2.keys()))
        res = []
        for key in keys:
            l = min(d1[key], d2[key])
            res.extend([key] * l)
        return res

    def intersect2(self, nums1, nums2):
        d1 = dict()
        for n in nums1:
            d1[n] = d1.get(n, 0) + 1
        
        res = []
        for n in nums2:
            if n in d1:
                res.append(n)
                d1[n] -= 1
                if d1[n] == 0:
                    del d1[n]
        return res