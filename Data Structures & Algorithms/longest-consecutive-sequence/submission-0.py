class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxSeq = 0
        for num in nums:
            if num - 1 not in nums: # If start of seq
                seq = 0
                while num + seq in nums:
                    seq += 1
                
                maxSeq = max(seq, maxSeq)
        return maxSeq
        