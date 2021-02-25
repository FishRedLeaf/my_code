class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int i = 0;
        int res = nums[0] + nums[1] + nums[2];
        int min_abs = abs(res - target);
        for (auto iter = nums.begin(); iter <= nums.end() - 3;) {
            auto left = iter + 1;
            auto right = nums.end() - 1;
            while (left < right) {
                int val = *iter + *left + *right;
                if (val == target) {
                    return val;
                } else if (val < target) {
                    if (abs(val - target) < min_abs) {
                        min_abs = abs(val - target);
                        res = val;
                    }
                    left += 1;
                } else {
                    if (abs(val - target) < min_abs) {
                        min_abs = abs(val - target);
                        res = val;
                    }
                    right -= 1;
                }
            }
            iter += 1;
        }
        return res;
    }
};