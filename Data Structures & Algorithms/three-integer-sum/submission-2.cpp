class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        set<vector<int>> res;
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] > 0) { break; } // smallest is bigger than 0
            if (i > 0 && nums[i] == nums[i - 1]) { continue; } // skip to unique

            int l = i + 1; // left
            int r = nums.size() - 1; // right

            while (l < r) {
                int sum = nums[i] + nums[l] + nums[r];

                if (sum > 0) { r--; }
                else if (sum < 0 ) { l++; }
                else { // match
                    res.insert({nums[i], nums[l], nums[r]}); 
                    l++; r--;
                    while (l < r && nums[l] == nums[l - 1]) { l++; }
                }
            }
        }

        return vector<vector<int>>(res.begin(), res.end());
    }
};