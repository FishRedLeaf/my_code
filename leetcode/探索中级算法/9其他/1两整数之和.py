'''
不使用运算符 + 和 - ​​​​​​​，计算两整数 ​​​​​​​a 、b ​​​​​​​之和。

示例 1:

输入: a = 1, b = 2
输出: 3
示例 2:

输入: a = -2, b = 3
输出: 1
'''

class Solution:
    def getSum(self, a: int, b: int) -> int:

        ans = 0
        mask = 0x01
        carry = 0
        for _ in range(32):
            x, y = a&mask, b&mask
            c = carry
            carry = 0
            if x ^ y != 0:
                if c == 1:
                    carry = 1
                else:
                    ans |= mask
            else:
                if x & mask > 0:
                    carry = 1
                if c == 1:
                    ans |= mask
            mask <<= 1
        if ans > 0x7fffffff:
            return ans - 0xffffffff - 1
        return ans
    
print(Solution().getSum(-5,6))