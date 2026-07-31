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
        meetings = []
        for interval in intervals:
            idx = bisect_left(meetings,interval.start,key=lambda x: x.start)
            meetings.insert(idx, interval)
        
        for i in range(1,len(meetings)):
            if meetings[i].start < meetings[i-1].end:
                return False

        return True