class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj_list = {}
        n = len(equations)
        for i in range(n):
            n1, n2 = equations[i]
            adj_list[n1] = adj_list.get(n1, {})
            adj_list[n1][n2] = values[i]
            adj_list[n2] = adj_list.get(n2, {})
            adj_list[n2][n1] = 1/values[i]

        res = []
        for n1, n2 in queries:
            q = deque([(n1, 1)])
            visited = set()
            ans = -1
            while q:
                node, score = q.popleft()
                visited.add(node)
                if node not in adj_list:
                    break
                for nei in adj_list[node]:
                    if nei == n2:
                        ans = score * adj_list[node][n2]
                        q = None
                        break
                    elif nei not in visited:
                        q.append([nei, score * adj_list[node][nei]])

            res.append(ans)
        return res