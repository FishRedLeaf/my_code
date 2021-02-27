import "sort"
func fourSum(nums []int, target int) [][]int {
	if (len(nums) < 4) {
        return make([][]int, 0)
	}
	sort.Ints(nums)
	i := 0
    res := make([][]int, 0)
	for (i <= len(nums) - 4) {
		if (i >= 1 && nums[i] == nums[i-1]) {
			i += 1
			continue
		}
		j := i + 1
		for (j <= len(nums) - 3) {
			if (j >= i + 2 && nums[j] == nums[j-1]) {
				j += 1
				continue
			}
			left, right := j + 1, len(nums) - 1
			for (left < right) {
				val := nums[i] + nums[j] + nums[left] + nums[right]
				if (val == target) {
					res = append(res, []int{nums[i], nums[j], nums[left], nums[right]})
					left += 1
					right -= 1
					for (left <right && nums[left] == nums[left-1]) {
						left += 1
					} 
					for (left < right && nums[right] == nums[right+1]) {
						right -= 1
					}
				} else if (val < target) {
					left += 1
				} else {
					right -= 1
				}
			}
			j += 1
		}
		i += 1
	}
	return res
}