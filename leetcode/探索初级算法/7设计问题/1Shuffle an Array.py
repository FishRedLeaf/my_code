'''
打乱一个没有重复元素的数组。

示例:

// 以数字集合 1, 2 和 3 初始化数组。
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// 打乱数组 [1,2,3] 并返回结果。任何 [1,2,3]的排列返回的概率应该相同。
solution.shuffle();

// 重设数组到它的初始状态[1,2,3]。
solution.reset();

// 随机返回数组[1,2,3]打乱后的结果。
solution.shuffle();
'''

import random
class Solution:

    def __init__(self, nums):
        self.nums = nums
        

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        """
        
        l = len(self.nums)
        idxs = list(range(l))
        shuffle_nums = []
        for _ in range(l):
            idx = random.randint(0,len(idxs)-1)
            k = idxs[idx]
            idxs.pop(idx)
            shuffle_nums.append(self.nums[k])
        return shuffle_nums
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()