class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        res = []
        intervals.sort(key = lambda x:x[0])
        cur = intervals[0]

        def overlapping(interval1, interval2):
            return not (interval1[0] > interval2[1] or interval1[1] < interval2[0])

        for i in range(1,len(intervals)):
            if overlapping(cur, intervals[i]):
                cur[0] = min(cur[0], intervals[i][0])
                cur[1] = max(cur[1], intervals[i][1])
            else:
                res.append(cur)
                cur = intervals[i]

        res.append(cur)
        return res
