class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqs = Counter(tasks)
        heap = []
        heapq.heapify_max(heap)
        for c in freqs:
            heapq.heappush_max(heap, (freqs[c],c))

        most = heap[0][0]
        if most == 1:
            return len(heap)
        
        nummax = 0
        while heap:
            freq, c = heapq.heappop_max(heap)
            if freq == most:
                nummax += 1
            else: break
        return max(most + (most-1) * n + (nummax - 1), sum(freqs.values()))