class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            if target - n in nums[:i] + nums[i+1:]:
                return [nums.index(n) + 1, nums.index(target - n, i + 1) + 1]