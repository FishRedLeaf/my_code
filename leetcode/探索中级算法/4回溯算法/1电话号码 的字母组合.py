'''
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
说明:
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
'''

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        self.res = []
        if digits == '':
            return self.res
        self.dfs('', digits)
        return self.res
        
    def dfs(self, s, digits):
        if len(digits) == 0:
            self.res.append(s)
        else:
            ddd = {'2':['a','b','c'],
               '3':['d','e','f'],
               '4':['g','h','i'],
               '5':['j','k','l'],
               '6':['m','n','o'],
               '7':['p','q','r','s'],
               '8':['t','u','v'],
               '9':['w','x','y','z']}
            cur_digit = digits[0]
            for c in ddd[cur_digit]:
                self.dfs(s+c, digits[1:])

class Solution2(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
            
        d = {1: "", 2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
        
        def dfs(digits, index, path, res, d):
            if index == len(digits):
                res.append("".join(path))
                return
        
            digit = int(digits[index])
            for c in d.get(digit, []):
                path.append(c)
                dfs(digits, index + 1, path, res, d)
                path.pop()
        
        res = []
        dfs(digits, 0, [], res, d)
        return res