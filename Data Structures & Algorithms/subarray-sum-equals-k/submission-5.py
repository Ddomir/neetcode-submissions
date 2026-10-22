class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        totSum = 0
        sumCount = defaultdict(int)
        sumCount[0] = 1
        res = 0

        for i, n in enumerate(nums):
            totSum += n

            res += sumCount.get(totSum - k, 0)
            sumCount[totSum] += 1

        return res