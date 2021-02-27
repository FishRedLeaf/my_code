class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        if (nums.size() <= 3) {
            return {};
        }
        sort(nums.begin(), nums.end());
        int i = 0;
        vector<vector<int>> res;
        for (auto iter = nums.begin(); iter <= nums.end() - 4;) {
            if (iter >= nums.begin() + 1 && *iter == *(iter-1)) {
                iter += 1;
                continue;
            }
            for (auto iter2 = iter + 1; iter2 <= nums.end() - 3;) {
                if (iter2 >= iter + 2 && *iter2 == *(iter2-1)) {
                    iter2 += 1;
                    continue;
                }
                auto left = iter2 + 1;
                auto right = nums.end() - 1;
                while (left < right) {
                    int val = *iter + *iter2 + *left + *right;
                    if (val == target) {
                        res.push_back({*iter, *iter2, *left, *right});
                        for (auto prev = left; left < right && *left == *prev; ++left);
                        for (auto prev = right; left < right && *right == *prev; --right);
                    } else if (val < target) {
                        left += 1;
                    } else {
                        right -= 1;
                    }
                }
                iter2 += 1;
            }
            iter += 1;
        }
        return res;
    }
};