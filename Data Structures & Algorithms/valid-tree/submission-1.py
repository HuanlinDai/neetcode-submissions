class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        graph = {}
        for u, v in edges:
            graph[u] = graph.get(u,[]) + [v]
            graph[v] = graph.get(v,[]) + [u]
        
        visit = set()
        def dfs(u, prev):
            if u in visit:
                return False
            visit.add(u)
            for v in graph.get(u,[]):
                if v == prev:
                    continue
                if not dfs(v,u):
                    return False

            return True
        return dfs(0,-1) and len(visit) == n