#
# @lc app=leetcode.cn id=677 lang=python3
#
# [677] 键值映射
#

 %#56.72%
# class MapSum:

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.d = {}

#     def insert(self, key: str, val: int) -> None:
#         self.d[key] = val

#     def sum(self, prefix: str) -> int:
#         res = 0
#         for k, v in self.d.items():
#             if k.startswith(prefix):
#                 res += v
#         return res


# 
class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, key: str, val: int) -> None:
        node = self.root
        for letter in key:
            # setdefault 如果字典中包含有给定键，
            # 则返回该键对应的值，否则返回为该键设置的值
            node = node.setdefault(letter, {})
        node['end'] = val

    def sum(self, prefix: str) -> int:
        node = self.root
        for letter in prefix:
            node = node.setdefault(letter, {})
        self.res = 0

        def dfs(node):
            for k, v in node.items():
                if k == 'end':
                    self.res += v
                else:
                    dfs(v)
        dfs(node)
        return self.res

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)

