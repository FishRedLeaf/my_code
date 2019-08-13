class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        
        res = []
        cur_word = ''
        for c in s:
            if c != ' ':
                cur_word += c
            else:
                if cur_word:
                    res.append(cur_word)
                    cur_word = ''
        if cur_word:
            res.append(cur_word)
        return ' '.join(res)[::-1]
            