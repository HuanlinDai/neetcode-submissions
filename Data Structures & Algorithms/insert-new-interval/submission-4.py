from bisect import bisect_left
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        idx = bisect_left(intervals, newInterval)
        intervals.insert(idx, newInterval)
        # print(intervals)
        while len(intervals) > idx+1 and intervals[idx+1][0] <= newInterval[1]:
            intervals[idx][1] = max(intervals[idx][1], intervals[idx+1][1])
            intervals[idx][0] = min(intervals[idx][0], intervals[idx+1][0])
            intervals.pop(idx+1)
        # print(intervals)
        while idx > 0 and intervals[idx-1][1] >= newInterval[0]:
            intervals[idx][1] = max(intervals[idx][1], intervals[idx-1][1])
            intervals[idx][0] = min(intervals[idx][0], intervals[idx-1][0])
            intervals.pop(idx-1)
            idx -= 1
        # print(intervals)
        return intervals