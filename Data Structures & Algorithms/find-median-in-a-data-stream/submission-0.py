import heapq
class MedianFinder:

    def __init__(self):
        self.heap = []
        heapq.heapify(self.heap)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.heap, num)
        return None
    def findMedian(self) -> float:
        n = len(self.heap)
        last_two = heapq.nsmallest((n//2) + 1, self.heap)[-2:]

        if n%2:
            return float(last_two[-1])
        else:
            return sum(last_two)/2
        