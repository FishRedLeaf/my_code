#
# @lc app=leetcode.cn id=648 lang=python3
#
# [648] 单词替换
#
class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        root = {}
        
        for word in dict:
            node = root
            for letter in word:
                node = node.setdefault(letter, {})
            node['end'] = True
        
        res = []
        for word in sentence.split():
            node = root
            prefix = ''
            flag = False  # 表示当前单词是否有前缀
            for letter in word:
                prefix += letter
                node = node.setdefault(letter, {})
                if 'end' in node:
                    flag = True
                    res.append(prefix)
                    break
            if not flag:
                res.append(word)
        return ' '.join(res)

