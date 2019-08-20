#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return []
        if len(triangle) == 1:
            return triangle[0][0]
        n = len(triangle)
        pre = [triangle[0][0]]
        for i, cur_layer in enumerate(triangle):
            if i >= 1:
                cur = [cur_layer[0] + pre[0]]
                for j in range(1, i):
                    cur.append(cur_layer[j] + min(pre[j], pre[j-1]))
                cur.append(pre[-1] + cur_layer[-1])
                pre = cur
        return min(pre)


