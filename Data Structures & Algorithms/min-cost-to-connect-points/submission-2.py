class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        n = len(points)
        dist = [float('inf')] * n
        visited = [False] * n
        node = 0
        res = 0
        edges = 0

        while edges < n-1:
            visited[node] = True
            nextnode = -1
            for i in range(n):
                if visited[i]:
                    continue
                dist[i] = min(abs(points[i][0] - points[node][0]) + abs(points[i][1]-points[node][1]), dist[i])
                if nextnode == -1 or dist[i] < dist[nextnode]:
                    nextnode = i
            res += dist[nextnode]
            edges += 1
            node = nextnode

        return res
