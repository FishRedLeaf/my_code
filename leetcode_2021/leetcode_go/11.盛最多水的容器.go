import "math"

func maxArea(height []int) int {
	i, j := 0, len(height) - 1
	var maxArea float64 = 0
	for (i < j) {
        maxArea = math.Max(maxArea, float64(j-i) * math.Min(float64(height[i]), float64(height[j])))
		if (height[i] < height[j]) {
			i += 1
		} else {
			j -= 1
		}
	}
	return int(maxArea)
}