class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            j = i + 1
            while j < len(nums):
                if n + nums[j] == target:
                    if i > j:
                        return [j, i]
                    return [i, j]
                j += 1