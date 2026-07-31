class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        
        def overlapping(orig, new):
            return not (res[orig][0] > res[new][1] or res[orig][1]<res[new][0])

        for interval in intervals:
            idx = 0
            for oldinterval in res:
                if oldinterval[0] > interval[1]:
                    break
                elif oldinterval[1] < interval[0]:
                    idx += 1
                else:
                    break
            res.insert(idx,interval)
            # print(f'inserting {interval} at {idx}')
            # print(res)
            while 0 < idx and overlapping(idx-1,idx):
                # print(f'left merging {interval} with {res[idx-1]}')
                newstart = min(res[idx-1][0], res[idx][0])
                newend = max(res[idx-1][1], res[idx][1])
                res.pop(idx)
                res[idx] = [newstart, newend]
                idx -= 1
                
            while idx < len(res) - 1 and overlapping(idx+1,idx):
                # print(f'right merging {interval} with {res[idx-1]}')
                newstart = min(res[idx+1][0], res[idx][0])
                newend = max(res[idx+1][1], res[idx][1])
                res.pop(idx)
                res[idx] = [newstart, newend]
        return res