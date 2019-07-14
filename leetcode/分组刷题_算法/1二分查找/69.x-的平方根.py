#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        if x == 0:
            return 0
        l, r = 0, x-1
        while l <= r:
            # print(l, r)
            mid = l + ((r-l) >> 2)
            if mid * mid - x == 0:
                return mid
            elif mid * mid - x > 0:
                r = mid - 1
            else:
                l = mid + 1
        return r

# print(Solution().mySqrt(8))

