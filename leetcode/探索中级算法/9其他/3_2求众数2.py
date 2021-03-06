'''
给定一个大小为 n 的数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。

说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1)。

示例 1:

输入: [3,2,3]
输出: [3]
示例 2:

输入: [1,1,1,3,3,2,2,2]
输出: [1,2]
'''

class Solution:
    def majorityElement(self, nums):
        ddd = dict()
        for i in nums:
            ddd[i] = ddd.get(i, 0) + 1
        l = len(nums)//3
        res = []
        for k,v in ddd.items():
            if v > l:
                res.append(k)
        return res

print(Solution().majorityElement([3,2,3]))