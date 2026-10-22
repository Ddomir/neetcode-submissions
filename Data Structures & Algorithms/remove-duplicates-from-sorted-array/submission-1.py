class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dupCount = i = 0
        nextUnq = 1

        while dupCount + i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                while nextUnq + i < len(nums) and nums[i] == nums[i + nextUnq]:
                    nextUnq += 1
                
                nums[i+1:] = nums[i+nextUnq:]
                nums += [nums[i]] * (nextUnq - 1)
                i += 1
                dupCount += nextUnq - 1
                nextUnq = 1
            
            else:
                i += 1
        
        return len(nums) - dupCount