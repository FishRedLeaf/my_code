

class UnionFindSet:

    def __init__(self, n):
        self.father = list(range(n))
        self.rank = [0] * n
        self. count = n

    def find(self, x):
        father = self.father
        if father[x] != x:
            father[x] = self.find(father[x])
        return father[x]

    def union(self, x, y):
        father = self.father
        x, y = map(self.find, [x, y])
        if x == y:
            return False
        if self.rank[x] > self.rank[y]:
            father[y] = x
        else:
            father[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1
        self.count -= 1
        return True

    def getCount(self):
        return self.count
