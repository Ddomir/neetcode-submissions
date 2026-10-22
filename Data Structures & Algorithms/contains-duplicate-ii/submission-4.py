class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        lastKNums = set()

        for i in range(k): # Adding first k nums
            if nums[i] in lastKNums:
                return True
            lastKNums.add(nums[i])
        
        if k >= len(nums): # Should have already seen
            return False
        
        for i in range(k, len(nums)): # Checking rest
            if nums[i] in lastKNums:
                return True
            
            lastKNums.add(nums[i])
            lastKNums.remove(nums[i-k])
        
        return False