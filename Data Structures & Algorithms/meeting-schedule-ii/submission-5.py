"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        events = []
        for interval in intervals:
            events.append((interval.start, 1))
            events.append((interval.end, -1))

        events.sort(key = lambda x: (x[0], x[1]))
        print(events)
        res = cur = 0
        for i in range(len(events)):
            cur += events[i][1]
            res = max(res, cur)

        return res