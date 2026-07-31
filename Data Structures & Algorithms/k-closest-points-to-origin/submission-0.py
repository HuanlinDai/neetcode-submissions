class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        heap = []
        heapq.heapify(heap)
        for x,y in points:
            heapq.heappush(heap, (math.sqrt(x**2 + y**2), x, y))

        for i in range(k):
            d,x,y = heapq.heappop(heap)
            res.append([x,y])

        return res