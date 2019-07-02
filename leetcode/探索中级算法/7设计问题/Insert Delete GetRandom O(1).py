'''
设计一个支持在平均 时间复杂度 O(1) 下，执行以下操作的数据结构。

insert(val)：当元素 val 不存在时，向集合中插入该项。
remove(val)：元素 val 存在时，从集合中移除该项。
getRandom：随机返回现有集合中的一项。每个元素应该有相同的概率被返回。
示例 :

// 初始化一个空的集合。
RandomizedSet randomSet = new RandomizedSet();

// 向集合中插入 1 。返回 true 表示 1 被成功地插入。
randomSet.insert(1);

// 返回 false ，表示集合中不存在 2 。
randomSet.remove(2);

// 向集合中插入 2 。返回 true 。集合现在包含 [1,2] 。
randomSet.insert(2);

// getRandom 应随机返回 1 或 2 。
randomSet.getRandom();

// 从集合中移除 1 ，返回 true 。集合现在包含 [2] 。
randomSet.remove(1);

// 2 已在集合中，所以返回 false 。
randomSet.insert(2);

// 由于 2 是集合中唯一的数字，getRandom 总是返回 2 。
randomSet.getRandom();
'''

#python 列表的len()时间复杂度为o(1),所以可以不需要self.length
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ddd = {}
        self.vals = []
        self.length = 0
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.ddd:
            self.ddd[val] = self.length
            self.vals.append(val)
            self.length += 1
            return True
        return False


    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.vals:
            return False
        else:
            if self.length == 1:
                self.__init__()
            else:
                removeidx = self.ddd[val]
                self.vals[removeidx] = self.vals[-1]
                self.ddd[self.vals[-1]] = removeidx
                del self.ddd[val]
                del self.vals[-1]
                self.length -= 1
            return True


    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        import random
        return random.choice(self.vals)
        

class RandomizedSet2(object):

    def __init__(self):
        self.nums, self.pos = [], {}
        
    def insert(self, val):
        if val not in self.pos:
            self.nums.append(val)
            self.pos[val] = len(self.nums) - 1
            return True
        return False
        

    def remove(self, val):
        if val in self.pos:
            idx, last = self.pos[val], self.nums[-1]
            self.nums[idx], self.pos[last] = last, idx
            self.nums.pop(); self.pos.pop(val, 0)
            return True
        return False
            
    def getRandom(self):
        import random
        return self.nums[random.randint(0, len(self.nums) - 1)]

# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
print(obj.remove(0), obj.vals, obj.ddd)
print(obj.remove(0), obj.vals, obj.ddd)
print(obj.insert(0), obj.vals, obj.ddd)
print(obj.getRandom(), obj.vals, obj.ddd)
print(obj.remove(0), obj.vals, obj.ddd)
print(obj.insert(0), obj.vals, obj.ddd)

print()
obj = RandomizedSet2()
print(obj.remove(0), obj.nums, obj.pos)
print(obj.remove(0), obj.nums, obj.pos)
print(obj.insert(0), obj.nums, obj.pos)
print(obj.getRandom(), obj.nums, obj.pos)
print(obj.remove(0), obj.nums, obj.pos)
print(obj.insert(0), obj.nums, obj.pos)
