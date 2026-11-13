class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> seenNumbers;

        for (int number : nums) {
            if (seenNumbers.count(number)) {
                return true;
            }

            seenNumbers.insert(number);
        }

        return false;
    }
};