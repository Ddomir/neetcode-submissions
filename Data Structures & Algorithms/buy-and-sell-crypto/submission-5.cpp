class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.size() == 1) return 0;
        int res = 0;
        int l = 0; int r = 1;
        while (r < prices.size()) {
            res = max(res, prices[r] - prices[l]);
            if (prices[r] < prices[l]) l = r;

            r++;
        }
        return res;
    }
};
