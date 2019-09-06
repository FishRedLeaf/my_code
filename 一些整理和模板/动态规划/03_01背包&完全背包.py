# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 10:25:28 2019

@author: 鱼红叶

放到第i个物品时，背包剩余容量为j，此时选择放或不放
dp[j] = max(dp[j], dp[j-w[i]]+v[i])
"""
def bag_01(N, M, w, v):
    dp = [0] * (M+1)
    for i in range(1, N+1):
        for j in range(M, 0, -1):
            if j >= w[i]:
                dp[j] = max(dp[j], dp[j-w[i]]+v[i])
    return dp[-1]

def bag_full(N, M, w, v):
    dp = [0] * (M+1)
    for i in range(1, N+1):
        for j in range(1, M+1):
            if j >= w[i]:
                dp[j] = max(dp[j], dp[j-w[i]]+v[i])
    return dp[-1]

#import sys
#line = sys.stdin.readline().strip()
#N, M = list(map(int, line.split()))
#w, v = [0]*(N+1), [0]*(N+1)
#for i in range(1, N+1):
#    line = sys.stdin.readline().strip()
#    w[i], v[i] = list(map(int, line.split()))
    
#N, M = 4, 5
#w = [0, 1, 2, 3, 4]
#v = [0, 2, 4, 4, 5]
#print(bag_01(N, M, w, v))
    
    
N, M = 6, 20
v = [0,4,8,15,1,6,3]
w = [0,5,3,2,10,4,8]
print(bag_01(N,M,w,v))

N, M = 4, 6
v = [0,1,3,4,5]
w = [0,1,2,3,4]
print(bag_full(N,M,w,v))

