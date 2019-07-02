'''
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个位置。

示例 1:

输入: [2,3,1,1,4]
输出: true
解释: 从位置 0 到 1 跳 1 步, 然后跳 3 步到达最后一个位置。
示例 2:

输入: [3,2,1,0,4]
输出: false
解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。
'''

class Solution:
    def canJump(self, nums) -> bool:
        # method 1
        # max_step表示从当前位置能跳跃到的最远距离，在每个地方都计算一下
        max_step = 0
        for num in nums[:-1]:
            max_step = max(max_step - 1, num)
            if num == 0 and max_step == 0:
                return False
        return True   

    def canJump2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n == 0 or n == 1:
            return True
        idx, reach = 0, 0
        while idx < n-1 and idx <= reach:  
            # idx <= reach是为了处理nums[idx] == 0的情况，若idx>reach说明已经失败了
            print(idx, reach)
            reach = max(reach, idx+nums[idx])
            idx += 1
        print(idx, reach)
        return reach >= n-1

print(Solution().canJump2([3,2,1,0,4]))