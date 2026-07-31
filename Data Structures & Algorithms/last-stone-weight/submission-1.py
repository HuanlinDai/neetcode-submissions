class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap = stones
        heapq.heapify_max(heap)
        
        while len(heap) > 1:
            print(heap)
            w1, w2 = heapq.heappop_max(heap), heapq.heappop_max(heap)
            if w1 == w2:
                continue
            elif w1 > w2:
                heapq.heappush_max(heap, w1-w2)
            else:
                heapq.heappush_max(heap, w2-w1)
        if len(heap) == 1:
            return heap[0]
        return 0