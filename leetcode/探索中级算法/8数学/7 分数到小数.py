'''
给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以字符串形式返回小数。

如果小数部分为循环小数，则将循环的部分括在括号内。

示例 1:

输入: numerator = 1, denominator = 2
输出: "0.5"
示例 2:

输入: numerator = 2, denominator = 1
输出: "2"
示例 3:

输入: numerator = 2, denominator = 3
输出: "0.(6)"
'''

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        res = ''
        if numerator == 0:
            return str(numerator)
        if (numerator<0) ^ (denominator<0):
            res += '-'
        n = abs(numerator)
        d = abs(denominator)
        res += str(n // d)
        if (n % d == 0):
            return res
        res += '.'
        r = n % d
        ddd = {}
        while r:
            if r in ddd:
                res = res[:ddd[r]] + '(' + res[ddd[r]:] + ')'
                break
            ddd[r] = len(res)
            r *= 10
            res += str( r // d)
            r %= d
        return res
