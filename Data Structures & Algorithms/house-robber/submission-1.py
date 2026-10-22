class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        robbed = [0] * len(nums)
        robbed[0] = nums[0]
        robbed[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            robbed[i] = (max(nums[i] + robbed[i-2], robbed[i-1]))

        return max(robbed[-1], robbed[-2])