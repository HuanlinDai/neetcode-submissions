"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from bisect import bisect_left
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals: return True
        last_end = max(intervals, key = lambda x: x.end)
        meetings = [0] * (last_end.end + 1)
        for interval in intervals:
            meetings[interval.start] += 1
            meetings[interval.end] -= 1
        total = 0
        for i in range(len(meetings)):
            total += meetings[i]
            if total > 1:
                return False

        return True