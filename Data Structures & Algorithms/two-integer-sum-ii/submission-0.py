class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for n in nums:
            if target - n in nums:
                return [nums.index(n) + 1, nums.index(target - n) + 1]