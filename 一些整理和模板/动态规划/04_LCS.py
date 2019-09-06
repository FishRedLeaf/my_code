# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 21:27:17 2019

@author: 鱼红叶

https://www.cnblogs.com/CheeseZH/p/8830482.html
分为两种
1 最长公共子序列（Longest-Common-Subsequences）
2 最长公共子串（Longest-Common-Substring）

1看这个图
https://blog.csdn.net/littlethunder/article/details/25637173
代码
https://mp.weixin.qq.com/s/myJbSMpOkh2zCPoY4q3duw

2 看这个代码和图
https://blog.csdn.net/ggdhs/article/details/90713154

"""


def longestCommonSubsequence(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[-1][-1]

str1 = 'BDCABA'
str2 = 'ABCBDAB'
print(longestCommonSubsequence(str1, str2))

# 相对于上面那个，空间复杂度从O(n^2) -> O(n)
def longestCommonSubsequence2(str1, str2):
    m, n = len(str1), len(str2)
    pre, cur = [0] * (n+1), [0] * (n+1)
    for i in range(1, m+1):
        for j in range(1, n+1):
            if str1[i-1] == str2[j-1]:
                cur[j] = pre[j-1] + 1
            else:
                cur[j] = max(pre[j], cur[j-1])
        pre = cur
        cur = [0] * (n+1)
    return pre[-1]

print(longestCommonSubsequence2(str1, str2))


def longestCommonSubstring(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n+1) for _ in range(m+1)]
    res = 0
    for i in range(1, m+1):
        for j in range(1, n+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
                res = max(res, dp[i][j])
    return res

print(longestCommonSubstring("helloworld","loop"))
print(longestCommonSubstring(str1, str2))









