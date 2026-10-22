class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1

        maxVol = min(heights[l], heights[r]) * (r - l)

        while l < r:
            print(str(l) + " = " + str(heights[l]))
            print(str(r) + " = " + str(heights[r]))
            print(maxVol)
            print()
            if heights[l] < heights[r]:
                l += 1
                maxVol = max(maxVol, min(heights[l], heights[r]) * (r - l))

            else:
                r -= 1
                maxVol = max(maxVol, min(heights[l], heights[r]) * (r - l))
                
        return maxVol
        