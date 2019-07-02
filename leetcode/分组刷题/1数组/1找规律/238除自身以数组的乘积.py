'''
给定长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

示例:

输入: [1,2,3,4]
输出: [24,12,8,6]

input: [1,2,3,4,5]
A:[1, 1*2, 1*2*3, 1*2*3*4, 1*2*3*4*5]
B:[1*2*3*4*5, 2*3*4*5, 3*4*5, 4*4, 5]
output:
output[0] = B[1]
output[-1] = A[-2]
for i in range(1, l-1):
    output[i] = A[i-1] * B[i+1]
'''

class Solution:
    def productExceptSelf(self, nums):
        '''
        由于output[i] = nums[0]*nums[1]*...*nums[i-1]*nums[i+1]*...*nums[len-1],
        可以将output[i]分为两部分，前半部分为C[i] = nums[0]*nums[1]*...*nums[i-1],
        后半部分为D[i] = nums[i+1]*...*nums[len-1]。可以发现规律，数组C和D相邻元素之间存在递推关系：
        C[i] = C[i-1]*nums[i-1] (i = 1~len-1)
        D[i] = D[i+1]*nums[i+1] (i = 0~len-2)
        '''
        l = len(nums)
        A = [nums[0]] * l
        B = [nums[-1]] * l
        for i in range(1, l):
            A[i] = A[i-1] * nums[i]
        for i in range(l-2, -1, -1):
            B[i] = B[i+1] * nums[i]
        
        res = [0] * l
        res[0] = B[1]
        res[l-1] = A[l-2]
        for i in range(1, l-1):
            res[i] = A[i-1] * B[i+1]
    
        return res

print(Solution().productExceptSelf([1,2,3,4]))