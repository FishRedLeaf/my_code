'''
给定一个Excel表格中的列名称，返回其相应的列序号。

例如，

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
示例 1:

输入: "A"
输出: 1
示例 2:

输入: "AB"
输出: 28
示例 3:

输入: "ZY"
输出: 701
致谢：
特别感谢 @ts 添加此问题并创建所有测试用例。
'''

class Solution:
    def titleToNumber(self, s: str) -> int:
        letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        letters = [c.upper() for c in letters]
        values  = [ord(c)-64 for c in letters]
        ddd = dict(zip(letters, values))
        
        res = 0
        x = 1
        for c in s[::-1]:
            res += x * ddd[c]
            x *= 26
        
        return res

    def titleToNumber2(self, s: str) -> int:
        
        res = 0
        x = 1
        for c in s[::-1]:
            res += x * (ord(c)-ord('A')+1)
            x *= 26
        
        return res

print(Solution().titleToNumber2('ZY'))
