class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(combo, remaining, ind):
            if remaining == 0:
                res.append(combo[:])
                return
            
            if remaining < 0:
                return
            
            for i in range(ind, len(nums)):
                combo.append(nums[i])
                dfs(combo, remaining - nums[i], i)
                combo.pop()
        
        dfs([], target, 0)
        return res