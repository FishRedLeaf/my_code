
"""
牛客上看到的一道华为面试题

牛客试题广场有
https://www.nowcoder.com/questionTerminal/28c1dc06bc9b4afd957b01acdf046e69

博客上解法
https://blog.csdn.net/eurus_5bb67476/article/details/77197268


给定一个字符串s，你可以从中删除一些字符，使得剩下的串是一个回文串。
如何删除才能使得回文串最长呢？ 输出需要删除的字符个数。

  （1）把字符串旋转形成另外一个字符串，称为旋转字符串；
  （2）求原字符串s1与旋转字符串s2中，最长公共子序列的长度；
  （3）删除的字符数目 = 原字符串的长度 - 最长公共子序列的长度。

  *** 子序列可以是不连续的，子串必须连续！！！！！
  注意与leetcode718的区别！！！
"""

def solution(s):
    t = s[::-1]
    n = len(s)
    dp = [[0] * (n+1) for _ in range(n+1)]
    for i in range(n-1, -1, -1):
        for j in range(n-1, -1, -1):
            if s[i] == t[j]:
                dp[i][j] = 1 + dp[i+1][j+1]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j+1])
    # print(dp)
    return n - max(max(row) for row in dp)

# print(solution('aaab'))
# print(solution('abcda'))
# print(solution('google'))

if __name__ == '__main__':
    while True:
        line = sys.stdin.readline().strip()
        if not line:
            break
        print(solution(line))