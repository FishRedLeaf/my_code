"""
给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字母的最小子串。

示例：

输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"

说明：


    如果 S 中不存这样的子串，则返回空字符串 ""。
    如果 S 中存在这样的子串，我们保证它是唯一的答案。"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        可行子串：包含t的所有字母
        达到可行的条件：
        1 dict_t中的每个键都在dict_window中
        2 dict_t中的每个键的值都小于等于dict_window中对应键的值
        不满足可行窗口时增大r
        当一个窗口满足可行窗口的条件后，尝试缩小窗口大小，增大l
        当窗口不再满足是可行窗口时，退出缩小窗口的循环，继续增大r
        """

        if not s or not t or len(s) < len(t):
            return ""
        dict_t = {}
        for c in t:
            dict_t[c] = dict_t.get(c, 0) + 1

        dict_window = {}
        required = len(dict_t)
        formed = 0
        l, r = 0, 0
        ans = float('inf'), None, None

        while r < len(s):
            c = s[r]
            dict_window[c] = dict_window.get(c, 0) + 1
            # 注意一定要是==而不是>=，否则会重复计算多次c是匹配的
            if c in dict_t and dict_window[c] == dict_t[c]:
                formed += 1

            while l <= r and formed == required:
                if r - l + 1 < ans[0]:
                    ans = r- l + 1, l, r
                c = s[l]
                dict_window[c] -= 1
                if c in dict_t and dict_t[c] > dict_window[c]:
                    formed -= 1
                l += 1
            r += 1
        return "" if ans[0] == float('inf') else s[ans[l]:ans[r]+1]


