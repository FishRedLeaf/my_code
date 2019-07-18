
import random

def partition(nums, left, right):
    p = random.randint(left, right)
    pv = nums[p]
    nums[p], nums[right] = nums[right], nums[p]
    mid = left
    for i in range(left, right):
        # 比pv小的放到左边，大的放到右边
        if nums[i] <= pv:
            nums[i], nums[mid] = nums[mid], nums[i]
            mid += 1
    nums[mid], nums[right] = nums[right], nums[mid]
    return mid

def quick_sort(nums, left, right):
    if right <= left:
        return
    mid = partition(nums, left, right)
    quick_sort(nums, left, mid-1)
    quick_sort(nums, mid+1, right)


nums = [3,2,4,8,1]
quick_sort(nums, 0, len(nums)-1)
print(nums)

