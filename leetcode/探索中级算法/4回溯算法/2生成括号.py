'''
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''
class Solution2(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.res = []
        self.singleStr('', 0, 0, n)
        return self.res
    
    def singleStr(self, s, left, right, n):
        if left==n and right==n:
            self.res.append(s)
        if left < n:
            self.singleStr(s+'(', left+1, right, n)
        if right < left:
            self.singleStr(s+')', left, right+1, n)
            
#由Solution3改进而来
class Solution4(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def dfs(left, s, res, n):
            if len(s) == 2*n:
                if left == 0:
                    res.append(s)
                return
            if left < n:
                dfs(left+1, s+'(', res, n)
            if left > 0:
                dfs(left-1, s+')', res, n)
            
        res = []
        dfs(0, '', res, n)
        return res

class Solution3(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def dfs(left, path, res, n):
            if len(path) == 2 * n:
                if left == 0:
                    res.append("".join(path))
                return
            
            if left < n:
                path.append("(")
                dfs(left + 1, path, res, n)
                path.pop()
            if left > 0:
                path.append(")")
                dfs(left - 1, path, res, n)
                path.pop()
            
        res = []
        dfs(0, [], res, n)
        return res

#笨比方法，全排列+括号匹配，超时
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        alist = ['('] * n + [')'] * n
        res = self.fullPermutation(alist)
        Parenthesis = []
        for a in res:
            if self.ifmatch(a):
                Parenthesis.append(a)
        return Parenthesis
    
    def fullPermutation(self, alist):
        if not alist:
            return ''
        if len(alist) == 1:
            return alist
        res = []
        for i,a in enumerate(alist):
            rest = alist[:i] + alist[i+1:]
            for j in self.fullPermutation(rest):
                if a+j not in res:
                    res.append(a + j)
        return res
    
    def ifmatch(self, s):
        stack = []
        for c in s:
            if c == '(':
                stack.append(c)
            else:
                if not stack:
                    return False
                popItem = stack.pop()
                if popItem != '(':
                    return False
        return True
                
Parenthesis = Solution().generateParenthesis(3)
print(Parenthesis)
print(len(Parenthesis))
print(Solution().ifmatch('((()))'))