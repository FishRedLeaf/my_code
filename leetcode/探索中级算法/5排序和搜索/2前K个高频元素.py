'''
给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

示例 1:

输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
示例 2:

输入: nums = [1], k = 1
输出: [1]
说明：

你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
'''
class Solution:
    def topKFrequent(self, nums, k):
        num2count = dict()
        for n in nums:
            num2count[n] = num2count.get(n, 0) + 1
        counts = list(num2count.values())
        counts.sort(reverse=True)
        sel_counts = counts[:k]
        res = []
        for key, val in num2count.items():
            if val in sel_counts:
                res.append(key)
        return res

print(Solution().topKFrequent([1,1,1,2,2,3], 2))