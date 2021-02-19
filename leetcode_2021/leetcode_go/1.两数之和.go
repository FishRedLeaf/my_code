func twoSum(nums []int, target int) []int {
    d := make(map[int]int)
    for i := 0; i < len(nums); i ++ {
        another := target - nums[i]
        if idx, ok := d[another]; ok {
            return []int{idx, i}
        }
        d[nums[i]] = i
    }
    return nil
}