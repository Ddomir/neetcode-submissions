class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        seen = collections.defaultdict(int)
        res = []

        for num in nums:
            seen[num] += 1
        
        for k, v in seen.items():
            if v > (len(nums)) // 3:
                res.append(k)

        return res
        