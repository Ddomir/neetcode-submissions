class Solution {
public:
    int maxArea(vector<int>& heights) {
        int l = 0;
        int r = heights.size()-1;
        int maxSoFar = 0;

        while (l<r) {
            int v = (r-l) * min(heights[l], heights[r]);
            if (v > maxSoFar) { maxSoFar = v; }
            if (heights[l] < heights[r]) {
                l++; 
            } else { r--; }
        }

        return maxSoFar;
    }
};
