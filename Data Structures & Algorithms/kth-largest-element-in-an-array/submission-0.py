import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.heap = [-1 * nums[i] for i in range(len(nums))]
        heapq.heapify(self.heap)

        for i in range(k):
            num = heapq.heappop(self.heap)

        return num * -1