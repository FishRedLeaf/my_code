'''给定一个未排序的数组，判断这个数组中是否存在长度为 3 的递增子序列。

数学表达式如下:

如果存在这样的 i, j, k,  且满足 0 ≤ i < j < k ≤ n-1，
使得 arr[i] < arr[j] < arr[k] ，返回 true ; 否则返回 false 。
说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1) 。

示例 1:

输入: [1,2,3,4,5]
输出: true
示例 2:

输入: [5,4,3,2,1]
输出: false
'''
#注意！！！！！子序列，而不是连续子序列
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a = b = float('inf')
        for n in nums:
            if a >= n:
                a = n
            elif b >= n:
                b = n
            else:
                return True
        return False
                
print(Solution().increasingTriplet([400,200,300,20,10,500]))