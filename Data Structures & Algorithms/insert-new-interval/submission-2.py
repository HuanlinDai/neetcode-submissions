class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        preceding = 0
        merge = 0
        n = len(intervals)
        for i in range(n):
            starti, endi = intervals[i]
            if endi < newInterval[0]:
                preceding += 1
            elif newInterval[0] <= starti <= newInterval[1] or \
                newInterval[0] <= endi <= newInterval[1] or \
                starti <= newInterval[0] <= endi or \
                starti <= newInterval[1] <= endi:
                merge += 1
            else:
                break
        print(f'preceding: {preceding}, merge {merge}')
        newStart, newEnd = newInterval
        for _ in range(merge):
            oldstart, oldend = intervals.pop(preceding)
            newStart = min(newStart, oldstart)
            newEnd = max(newEnd, oldend)
        intervals.insert(preceding, [newStart, newEnd])
        return intervals