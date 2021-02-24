import "sort"

func threeSum(nums []int) [][]int {
    if (len(nums) < 3) {
        return make([][]int, 0)
    }
    sort.Ints(nums)
    if (nums[0] > 0 || nums[len(nums)-1] < 0) {
        return make([][]int, 0)
    }
	i := 0
	res := make([][]int, 0)
    for (i <= len(nums) - 3 && nums[i] <= 0) {
        if (i >= 1 && nums[i] == nums[i-1]) {
            i += 1
			continue
        }
		left, right := i + 1, len(nums) - 1
        for (left < right) {
            if (nums[i] + nums[left] + nums[right] == 0) {
                res = append(res, []int{nums[i], nums[left], nums[right]})
                left += 1
                right -= 1
                for (left < right && nums[left] == nums[left-1]) {
                    left += 1
                }
                for (left < right && nums[right] == nums[right+1]) {
                    right -= 1
                }
            } else if (nums[i] + nums[left] + nums[right] < 0) {
                left += 1
            } else {
                right -= 1   
            }
        }
		i += 1
    }
	return res
}