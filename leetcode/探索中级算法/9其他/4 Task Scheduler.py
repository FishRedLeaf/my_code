'''
给定一个用字符数组表示的 CPU 需要执行的任务列表。其中包含使用大写的 A - Z 字母表示的26 种不同种类的任务。任务可以以任意顺序执行，并且每个任务都可以在 1 个单位时间内执行完。CPU 在任何一个单位时间内都可以执行一个任务，或者在待命状态。

然而，两个相同种类的任务之间必须有长度为 n 的冷却时间，因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。

你需要计算完成所有任务所需要的最短时间。

示例 1：

输入: tasks = ["A","A","A","B","B","B"], n = 2
输出: 8
执行顺序: A -> B -> (待命) -> A -> B -> (待命) -> A -> B.
注：

任务的总个数为 [1, 10000]。
n 的取值范围为 [0, 100]。
'''

class Solution:
    def leastInterval(self, tasks, n: int) -> int:
        ddd = {}
        for t in tasks:
            ddd[t] = ddd.get(t, 0) + 1
        max_ = 0
        for _,v in ddd.items():
            max_ = max(max_, v)
        
        count = 0
        for _,v in ddd.items():
            if v == max_:
                count += 1
        return max(len(tasks), (max_-1)*(n+1) + count)

    def leastInterval2(self, tasks, n: int) -> int:
        length = len(tasks)
        if length==1:
            return 1
        output = [0]*26
        for i in tasks:
            output[ord(i)-ord('A')] += 1
 
        count = 0
        max_o = max(output)
        for i in output:
            if i == max_o:
                count = count+1
                    
        return max(length, (max_o-1)*(n+1)+count)
    
print(Solution().leastInterval2(["A","A","A","B","B","B"],2))