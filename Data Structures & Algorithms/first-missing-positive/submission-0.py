class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        smPos = 1

        while smPos in nums:
            smPos += 1

        return smPos