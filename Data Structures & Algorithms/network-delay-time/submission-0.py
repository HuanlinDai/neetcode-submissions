class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        edges = {}
        visited = set()
        for u, v, t in times:
            edges[u] = edges.get(u,[]) + [(v,t)]
        
        heap = [(0,k)]
        res = 0
        while heap:
            curdist, u = heapq.heappop(heap)
            if u in visited:
                continue
            visited.add(u)
            res = curdist
            if u not in edges:
                continue
            for v, w in edges[u]:
                if v not in visited:
                    heapq.heappush(heap, (curdist+w, v))
        
        if len(visited) == n:
            return res
        return -1

            