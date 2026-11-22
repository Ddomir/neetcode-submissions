class Solution {
public:
    int search(vector<int>& nums, int target) {
        int shift = findShift(nums);
        int n = nums.size();

        int l = 0; int r = n - 1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            int real = (mid + shift) % n;
            if (nums[real] == target) return real; 
            if (nums[real] < target) l = mid + 1;
            else r = mid - 1;
        }
        return -1;
    }

private:
    int findShift(vector<int>& nums) {
         int shift;
        int l = 0; int r = nums.size() - 1; int mid;
        while (l < r) {
            mid = l + (r - l) / 2;
            if (nums[mid] > nums[r]) l = mid + 1;
            else r = mid;
        }
        return l;
    }
};
