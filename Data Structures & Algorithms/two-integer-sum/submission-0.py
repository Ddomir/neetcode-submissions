class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nHash = {}

        for i, n in enumerate(nums):
            if (target - n) in nHash and i != nHash[target - n]:
                return [nHash[target - n], i]
            else:
                nHash[n] = i
