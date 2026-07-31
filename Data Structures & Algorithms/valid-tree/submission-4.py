class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjlist = {}
        for u, v in edges:
            adjlist[u] = adjlist.get(u,[]) + [v]
            adjlist[v] = adjlist.get(v,[]) + [u]

        visited = set()
        q = deque([(0,None)])

        while q:
            node, parent = q.popleft()
            if node in visited:
                return False
            visited.add(node)
            if node not in adjlist:
                continue
            for v in adjlist[node]:
                if v != parent:
                    q.append((v, node))
            
        return len(visited) == n

