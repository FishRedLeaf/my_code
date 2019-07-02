'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"
'''
'''
四种解法：暴力法，动态规划，中心扩展，Manacher
'''
class Solution(object):
    
    #暴力法,超出时间限制 O(n3),O(1)
    def longestPalindrome1(self, s):
        if not s:
            return ''
        length = 1
        ans = s[0]
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                tmp = s[i:j+1]
                if tmp == tmp[::-1]:
                    if len(tmp) > length:
                        length = len(tmp)
                        ans = tmp
        return ans

    #动态规划 O(n2),O(n2)
    #f(i,j) = s[i]==s[j] if j-i<=1
    #f(i,j) = s[i]==s[j] and f(i+1,j-1) if j-i>1
    def longestPalindrome2(self, s):
        n = len(s)
        matrix = [[0 for i in range(n)] for i in range(n)]
        logestSubStr = ""
        logestLen = 0
 
        for j in range(0, n):
            for i in range(0, j+1):
                if j - i <= 1:
                    if s[i] == s[j]:
                        matrix[i][j] = 1
                        if logestLen < j - i + 1:
                            logestSubStr = s[i:j+1]
                            logestLen = j - i + 1
                else:
                    if s[i] == s[j] and matrix[i+1][j-1]:
                        matrix[i][j] = 1
                        if logestLen < j - i + 1:
                            logestSubStr = s[i:j+1]
                            logestLen = j - i + 1
        return logestSubStr


    #改进DP，O(n2),O(n)
    #f(?,j)仅由f(?,j-1)决定，因此只需要O(2n)的空间即可。
    #     j-1=2  j=3
    #i=0  (0,2)  -(0,3)
    #i=1  (1,2)- ~(1,3)
    #i=2  (2,2)~  (2,3)
    #i=3          (3,3) ()内表示(i,j)
    #上述例子表示(0,3)由(1,2)决定，(1,3)由(2,2)决定。其他情况j-i<=1,只需要考虑s[i]==s[j]

    def longestPalindrome3(self, s):
        n = len(s)
        lastList = [0] * n
        curList = [0] * n
        logestSubStr = ""
        logestLen = 0
 
        for j in range(0, n):
            for i in range(0, j + 1):
                if j - i <= 1:
                    if s[i] == s[j]:
                        curList[i] = 1
                        len_t = j - i + 1
                        if logestLen < len_t:
                            logestSubStr = s[i:j + 1]
                            logestLen = len_t
                else:
                    if s[i] == s[j] and lastList[i+1]:
                        curList[i] = 1
                        len_t = j - i + 1
                        if logestLen < len_t:
                            logestSubStr = s[i:j + 1]
                            logestLen = len_t
            lastList = curList
            curList = [0] * n
        return logestSubStr

print(Solution().longestPalindrome3('aaaa'))
