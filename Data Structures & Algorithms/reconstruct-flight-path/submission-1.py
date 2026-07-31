class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        tickets.sort()
        edges = {}
        for u, v in tickets:
            edges[u] = edges.get(u,[]) + [v]

        res = ["JFK"]

        def dfs(node):
            if len(res) == 1 + len(tickets):
                return True
            if node not in edges:
                return False

            tmp = edges[node].copy()
            for i,v in enumerate(tmp):
                res.append(v)
                edges[node].pop(i)
                if dfs(v): return True
                edges[node].insert(i,v)
                res.pop()

            return False

        dfs("JFK")
        return res