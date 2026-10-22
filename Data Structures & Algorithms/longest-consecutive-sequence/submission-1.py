class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxSeq = 0
        for num in numSet:
            if num - 1 not in numSet: # If start of seq
                seq = 0
                while num + seq in numSet:
                    seq += 1
                
                maxSeq = max(seq, maxSeq)
        return maxSeq
        