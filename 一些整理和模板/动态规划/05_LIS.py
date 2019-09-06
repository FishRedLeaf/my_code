# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 14:54:18 2019

@author: 鱼红叶

leetcode300
https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/zui-chang-shang-sheng-zi-xu-lie-dong-tai-gui-hua-e/

进阶可查看leetcode354
"""

nums = [2,1,5,3,6,4,8,9,7,8,9]

"""
动态规划
数组dp保存每步子问题的最优解;
dp[i]代表含第i个元素的最长上升子序列的长度。
求解dp[i],向前遍历找出比i元素小的元素j,令dp[i] = dp[j]+1
"""
def lengthOfLIS(nums):
    if not nums:
        return 0
    L = len(nums)
    dp = [1] * L
    for i in range(L):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
print(lengthOfLIS(nums))
print()

"""
动态规划+二分
数组cells，保存最长上升子序列
对nums进行遍历，将每个元素二分插入cells中
    如果cells中元素都比这个元素小，那么将该元素插到cells的最后
    否则，用它覆盖cells中比他大的元素中的最小的那个

***关键点***  来自https://blog.csdn.net/yopilipala/article/details/60468359
这个cells不是LIS，它只是存储的对应长度LIS的最小末尾
cells[i]中存储的是所有长度为i+1的上升子序列中末尾值最小的那个

2,1,5,3,6,4,8,9,7,8,9
cells:
2
1
1,5
1,3
1,3,6
1,3,4
1,3,4,8
1,3,4,8,9
1,3,4,7,9注意此时长度为4的上升子序列有1,3,4,7和1,3,4,8，那么cells[4-1]=末尾最小值7
1,3,4,7,8
1,3,4,7,8,9
"""
def lengthOfLIS2(nums):
    n = len(nums)
    if n < 2:
        return n
    cells = [nums[0]]
    for num in nums[1:]:
        print(cells)
        if num > cells[-1]:
            cells.append(num)
            continue
        l, r = 0, len(cells)-1
        while l < r:
            mid = l + ((r-l) >> 1)
            if cells[mid] < num:
                l = mid + 1
            else:
                r = mid
        cells[l] = num
    print(cells)
    return len(cells)
print(lengthOfLIS2(nums))
