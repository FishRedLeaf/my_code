

"""
https://www.cnblogs.com/bigsaltfish/p/10067078.html
1 数组中有一个数只出现一次，其他数都出现了两次，找出这个数
2 数组中有两个数出现一次，其他数都出现两次，找出这两个数
3 数组中有一个数只出现一次，其他数都出现了k次，找出这个数
"""

def solution1(nums):
    n = len(nums)
    if n < 0:
        return None
    res = nums[0]
    for i in range(1, n):
        res ^= nums[i]
    return res

print(solution1([1,2,2,3,3,4,4]))


def solution2(nums):
    n = len(nums)
    if n < 0:
        return None
    tmp = nums[0]
    for i in range(1, n):
        tmp ^= nums[i]
    # 根据tmp中等于1的某一位进行分割
    # 因为tmp某一位为1，表明1和3在这一位是不同的，
    # 那么根据这一位为1/0将nums分为两类
    c = 0  # 表示需要右移几位
    while True:
        if tmp & 1 == 1:
            break
        c += 1
        tmp >>= 1
    nums1, nums2 = [], []
    for num in nums:
        if (num >> c) & 1 == 1:
            nums1.append(num)
        else:
            nums2.append(num)
    return solution1(nums1), solution1(nums2)

print(solution2([1,2,2,3,4,4]))


def solution3(nums, k):
    n = len(nums)
    if n <= k:
        return None
    res = []
    while nums:
        tmp = 0
        new_nums = []
        for num in nums:
            tmp += num&1
            num >>= 1
            if num != 0:
                new_nums.append(num)
        tmp = 1 if tmp%k != 0 else 0
        res.append(tmp)
        nums = new_nums
    return int(''.join(list(map(str, res[::-1]))), 2)
    
print(solution3([1,1,1,2,3,3,3,4,4,4], 3))








