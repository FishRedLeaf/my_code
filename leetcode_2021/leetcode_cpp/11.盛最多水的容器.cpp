class Solution {
public:
    int maxArea(vector<int>& height) {
        int i = 0;
        int j = height.size() - 1;
        int max_area = 0;
        while (i < j) {
            max_area = max(max_area, (j-i) * min(height[i], height[j]));
            if (height[i] < height[j]) {
                i += 1;
            } else {
                j -= 1;
            }
        }
        return max_area;
    }
};