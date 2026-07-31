class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        qres = {}
        intervals.sort(key = lambda x: x[0])
        n = len(intervals)
        heap = []
        i = 0
        for q in sorted(queries):
            
            while i < n and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(heap, (r-l+1,r))
                i += 1
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            if not heap:
                qres[q] = -1
            else:
                qres[q] = heap[0][0]

        return [qres[q] for q in queries]