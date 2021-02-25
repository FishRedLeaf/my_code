import "sort"

func abs(n int) int {
    if n < 0 {
        return -n
    }
    return n
}

func threeSumClosest(nums []int, target int) int {
    sort.Ints(nums)
    i := 0
    res := nums[0] + nums[1] + nums[2]
    min_abs := abs(res - target)
    for (i <= len(nums) - 3) {
        left, right := i + 1, len(nums) - 1
        for (left < right) {
            val := nums[i] + nums[left] + nums[right]
            if (val == target) {
                return val
            } else if (val < target) {
                if (abs(val - target) < min_abs) {
                    min_abs = abs(val - target)
                    res = val
                }
                left += 1
            } else {
                if (abs(val - target) < min_abs) {
                    min_abs = abs(val - target)
                    res = val
                }
                right -= 1
            }
        }
        i += 1
    }
    return res
}