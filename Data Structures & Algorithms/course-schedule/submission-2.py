class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        visited = set()
        stack = set()
        require = {}
        for u,v in prerequisites:
            require[u] = require.get(u,[]) + [v]
        def dfs(u):
            if u in stack:
                return False

            visited.add(u)
            stack.add(u)
            for v in require.get(u,[]):
                if not dfs(v):
                    return False
            stack.remove(u)
            return True

        i = 0
        while len(visited) < numCourses:
            if i not in visited:
                if not dfs(i):
                    return False
            i+=1
        return True
