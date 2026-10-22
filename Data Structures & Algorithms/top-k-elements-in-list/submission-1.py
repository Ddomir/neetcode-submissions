class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numFreq = defaultdict(int)
        res = []

        for n in nums:
            numFreq[n] += 1

        for _ in range(k):
            val = max(numFreq, key=numFreq.get)
            res.append(val)
            numFreq.pop(val)

        return res


        