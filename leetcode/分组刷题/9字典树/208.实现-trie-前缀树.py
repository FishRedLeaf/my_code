#
# @lc app=leetcode.cn id=208 lang=python3
#
# [208] 实现 Trie (前缀树)
#
# 在这儿交不了，
# Failed to test the solution. Please open the output channel for details.
# 执行用时 :196 ms, 在所有 Python3 提交中击败了58.77%的用户
# 内存消耗 :29.2 MB, 在所有 Python3 提交中击败了40.86%的用户

class TrieNode:
    def __init__(self):
        self.childs = dict()
        self.isWord = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for letter in word:
            child = node.childs.get(letter)
            if not child:
                child = TrieNode()
                node.childs[letter] = child
            node = child
        node.isWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for letter in word:
            child = node.childs.get(letter)
            if not child:
                return False
            node = child
        return node.isWord

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for letter in prefix:
            child = node.childs.get(letter)
            if not child:
                return False
            node = child
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

