class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = {}
        for u, v in prerequisites:
            graph[u] = graph.get(u,[]) + [v]

        visited = set()
        stack = set()
        res = []
        def dfs(u):
            if u in stack:
                return False

            stack.add(u)
            for v in graph.get(u,[]):
                if not dfs(v):
                    return False
            stack.remove(u)
            if u not in visited:
                res.append(u)
            visited.add(u)
            return True

        u = 0
        while len(visited) < numCourses:
            if u not in visited:
                if not dfs(u):
                    return []
            u += 1
        return res