class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minHeap = sorted(stones)
        heapq.heapify(minHeap)

        while len(minHeap) > 1:
            y = minHeap.pop()
            x = minHeap.pop()

            if x > y:
                x -= y
                heapq.heappush(minHeap, x)
            elif x < y:
                y -= x
                heapq.heappush(minHeap, y)
        
        return 0 if len(minHeap) == 0 else minHeap[0]
