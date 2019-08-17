#
# @lc app=leetcode.cn id=842 lang=python3
#
# [842] 将数组拆分成斐波那契序列
# https://leetcode-cn.com/problems/split-array-into-fibonacci-sequence/solution/dfshui-su-yong-quan-ju-bian-liang-resji-lu-fu-he-t/

class Solution:
    def splitIntoFibonacci(self, S):
        self.res = []
        num = S
        def dfs(num, count):
            if count >= 3 and len(num) == 0:
                return True
            for i in range(1, len(num)+1):
                if int(num[:i]) > 2**31-1:
                    break
                if i > 1 and num[0] == '0':
                    continue
                if count < 2:
                    self.res.append(int(num[:i]))
                    if dfs(num[i:], count+1):
                        return True
                    self.res.pop()
                else:
                    if self.res[-1] + self.res[-2] == int(num[:i]):
                        self.res.append(int(num[:i]))
                        if dfs(num[i:], count+1):
                            return True
                        self.res.pop()
            return False
        if dfs(num, 0):
            return self.res
        else:
            return []
# print(Solution().splitIntoFibonacci("123456579"))
