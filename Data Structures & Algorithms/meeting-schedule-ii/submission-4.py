"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals: return 0
        last_end = max(intervals, key = lambda x: x.end)
        meetings = [0] * (last_end.end + 1)
        for interval in intervals:
            meetings[interval.start] += 1
            meetings[interval.end] -= 1
        cur = 0
        res = 0
        for i in range(len(meetings)):
            cur += meetings[i]
            res = max(res,cur)

        return res