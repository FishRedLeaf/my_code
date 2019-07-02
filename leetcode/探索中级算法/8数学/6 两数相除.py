'''
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。

示例 1:

输入: dividend = 10, divisor = 3
输出: 3
示例 2:

输入: dividend = 7, divisor = -3
输出: -2
说明:

被除数和除数均为 32 位有符号整数。
除数不为 0。
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。本题中，如果除法结果溢出，则返回 231 − 1。
'''

# m = a0*2^0+a1*2^1+a2*2^2+…+an*2^K
# dividend = divisor * result + yushu
# result = 2^K + 2^(K-1) + … + 1

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        m = abs(dividend)
        n = abs(divisor)
        sign = 1 if ((dividend<0) ^ (divisor<0)) else -1
        
        res = 0
        while m >= n:
            t = n # a0 = a1 = …… = aK = n
            p = 1 # 2^k
            while m >= (t<<1):
                t <<= 1
                p <<= 1
            m -= t
            res += p

        res = res if sign==-1 else -res
        if res > 2147483647:
            return 2147483647
        if res < -2147483648:
            return -2147483648
        return res

print(Solution().divide(7, -3))


