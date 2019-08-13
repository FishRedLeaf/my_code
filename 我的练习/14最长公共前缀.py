##

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        i, j, idx = 0, 0, 0
        while j < len(strs) and i < len(strs[j]):
            if j == 0:
                c = strs[j][i]
            else:
                if c != strs[j][i]:
                    break

            if j == len(strs)-1:
                i += 1
                j = 0
                idx += 1
            else:
                j += 1

        return strs[0][:idx]