"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        times = {}
        for i in intervals:
            times[i.start] = times.get(i.start,0) + 1
            times[i.end] = times.get(i.end,0) - 1

        res = count = 0
        for t in sorted(times.keys()):
            count += times[t]
            res = max(res,count)

        return res