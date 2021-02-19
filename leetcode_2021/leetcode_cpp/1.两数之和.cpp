class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> d;
        for (int i = 0; i < sizeof(nums); i++) {
            auto iter = d.find(target - nums[i]);
            if (iter != d.end()) {
                return {d[target - nums[i]], i};
            }
            d[nums[i]] = i;
        }
        return {};
    }
};