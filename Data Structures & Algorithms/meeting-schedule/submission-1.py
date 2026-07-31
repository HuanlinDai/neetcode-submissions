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
        if not intervals:
            return True
        intervals.sort(key=lambda x: x.start)
        lastend = 0
        for interval in intervals:
            if interval.start >= lastend:
                lastend = interval.end
            else:
                return False
        return True