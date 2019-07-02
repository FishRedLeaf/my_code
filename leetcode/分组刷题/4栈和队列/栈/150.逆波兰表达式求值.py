#
# @lc app=leetcode.cn id=150 lang=python3
#
# [150] 逆波兰表达式求值
#
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in ["+", "-", "*", "/"]:
                p2 = int(stack.pop())
                p1 = int(stack.pop())
                if t == "+":
                    c = p1 + p2
                elif t == "-":
                    c = p1 - p2
                elif t == "*":
                    c = p1 * p2
                else:
                    c = int(p1 / p2)
                stack.append(c)
            else:
                stack.append(int(t))
        return stack[0]

# print(Solution().evalRPN(["2","1","+","3","*"]))

# -2//3 != int(-2/3) (-1, 0)
# print(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))

        

