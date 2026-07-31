class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        edgeDict = {}
        for n1, n2 in edges:
            edgeDict[n1] = edgeDict.get(n1,[]) + [n2]
            edgeDict[n2] = edgeDict.get(n2,[]) + [n1]
        
        res = 0
        visited = set({})

        def dfs(val) -> None:
            if val in visited:
                return None
            visited.add(val)
            for child in edgeDict.get(val,[]):
                if child not in visited:
                    dfs(child)
            return None
        

        while len(visited) < n:
            for i in range(n):
                if i not in visited:
                    res += 1
                    dfs(i)
        
        return res