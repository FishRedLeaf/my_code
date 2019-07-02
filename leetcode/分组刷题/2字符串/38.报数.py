#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 报数
#
class Solution:
    def countAndSay(self, n: int) -> str:
        ans = '1'
        n -= 1
        while n > 0:
            pre = ans[0]
            res = ''
            count = 1
            for i in range(1, len(ans)):
                if ans[i] == pre:
                    count += 1
                else:
                    res += str(count) + pre
                    pre = ans[i]
                    count = 1
            res += str(count) + pre
            ans = res
            n -= 1
        return ans

