class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        i = seenCount = 0

        while i < len(nums) - seenCount:
            if nums[i] in seen:
                n = nums.pop(i)
                nums.append(n)
                seenCount += 1
            else:
                seen.add(nums[i])
                i += 1
        return len(nums) - seenCount

        