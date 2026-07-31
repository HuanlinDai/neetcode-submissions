from bisect import bisect_left
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        sortedw = sorted(nums[:k])
        res = [sortedw[-1]]
        for i in range(len(nums)-k):
            idx = bisect_left(sortedw, nums[i])
            sortedw.pop(idx)
            idx = bisect_left(sortedw, nums[k+i])
            sortedw.insert(idx, nums[k+i])
            res.append(sortedw[-1])
        return res
            