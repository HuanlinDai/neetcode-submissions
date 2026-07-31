class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        edgeDict = {}
        for n1, n2 in edges:
            edgeDict[n1] = edgeDict.get(n1,[]) + [n2]
            edgeDict[n2] = edgeDict.get(n2,[]) + [n1]

        visited = set({})
        path = set({})
        
        def dfs(val, prevval):
 
            if val in path:
                return False

            path.add(val)
            for child in edgeDict.get(val,[]):
                if child != prevval:
                    if not dfs(child,val):
                        return False
            visited.add(val)
            return True
        if not dfs(0, None):

            return False

        return len(visited) == n