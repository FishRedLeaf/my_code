#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#
class Solution:
    def maxSlidingWindow(self, nums, k):
        
        res = []
        if not nums:
            return res

        if len(nums) >= k:
            deque = []  # 存放元素的索引
            for i in range(k):
                while deque and nums[deque[-1]] < nums[i]:
                    deque.pop()
                deque.append(i)
            
            # print(deque)
            for i in range(k, len(nums)):
                res.append(nums[deque[0]])
                while deque and nums[deque[-1]] < nums[i]:
                    deque.pop()
                while deque and deque[0] <= i-k:
                    deque.pop(0)
                deque.append(i)
                # print(deque)

            res.append(nums[deque[0]])
        return res
        

    # 18.77 %
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     res = []
    #     if  not nums:
    #         return res
    #     for i in range(len(nums)-k+1):
    #         res.append(max(nums[i:i+k]))
        
    #     return res

# print(Solution().maxSlidingWindow([1,3,1,2,0,5], 3))
