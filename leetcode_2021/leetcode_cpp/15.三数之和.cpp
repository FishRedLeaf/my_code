class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        if (nums.size() < 3) {
            return {};
        }
        sort(nums.begin(), nums.end());
        if (nums.front() > 0 || nums.back() < 0) {
            return {};
        }

        vector<vector<int>> a;
        for (auto iter = nums.begin(); iter <= nums.end()-3 && *iter <= 0; ) {
            if (iter >= nums.begin() + 1 && *iter == *(iter-1)) {
                iter += 1;
                continue;
            }
            auto left = iter + 1;
            auto right = nums.end() - 1;

            while (left < right) {
                const auto val = *iter + *left + *right;
                if (val == 0) {
                    a.push_back({*iter, *left, *right});
                    for (auto prev = left; left < right && *left == *prev; ++left);
                    for (auto prev = right; left < right && *right == *prev; --right);
                } else if (val < 0) {
                    for (; left < right && *iter + *left + *right < 0; ++left);
                } else {
                    for (; left < right && *iter + *left + *right > 0; --right);
                }
            }
            iter += 1;
        }
        return a;
    }
};