'''
根据逆波兰表示法，求表达式的值。

有效的运算符包括 +, -, *, / 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。

说明：

整数除法只保留整数部分。
给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。
示例 1：

输入: ["2", "1", "+", "3", "*"]
输出: 9
解释: ((2 + 1) * 3) = 9
示例 2：

输入: ["4", "13", "5", "/", "+"]
输出: 6
解释: (4 + (13 / 5)) = 6
示例 3：

输入: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
输出: 22
解释: 
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
'''
#注意python2中 -13/5 = -3, int(13*1. / 5) = -2
#python3中 -13//5 = -3, int(-13 / 5) = -2

#评论中的代码
class Solution2:
    def evalRPN(self, tokens) -> int:
            stack = []
            for i in tokens:
                try:
                    i = int(i)
                except:
                    # print("--",stack)
                    s1 = stack.pop()
                    s2 = stack.pop()
                    if i == "*":a = s1*s2
                    elif i == "/":a = int(s2/s1)
                    elif i == "+":a = s1+s2
                    elif i == "-":a = s2-s1
                    stack.append(a)
                else:
                    stack.append(i)
            return stack[0]

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for i in range(len(tokens)):
            if tokens[i] not in "+-*/":
                stack.append(int(tokens[i]))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(self.cal(op1,op2,tokens[i]))
        return stack[0]
    
    def cal(self, op1, op2, op):
        if op == '+': return op1 + op2
        elif op == '-': return op1-op2
        elif op == '*': return op1*op2
        else:
            return int(op1/op2)
            # return int(op1*1./op2) #在 python2中需要这么写
            # if op1*op2 >= 0: return op1 // op2
            # else: 
            #     return -(abs(op1) // abs(op2))



print(Solution2().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
            
        