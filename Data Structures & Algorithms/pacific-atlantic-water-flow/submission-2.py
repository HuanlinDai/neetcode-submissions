class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
    
        pacific, atlantic = set(), set()
        visited = set()
        m, n = len(heights), len(heights[0])

        def dfs(i,j,ocean,prev):
            if (i,j) in ocean or not (0<=i<m and 0<=j<n):
                return
            if heights[i][j] < prev:
                return
            
            ocean.add((i,j))
            dfs(i+1,j,ocean,heights[i][j])
            dfs(i-1,j,ocean,heights[i][j])
            dfs(i,j+1,ocean,heights[i][j])
            dfs(i,j-1,ocean,heights[i][j])

        for i in range(m):
            dfs(i,0,pacific,0)
            dfs(i,n-1,atlantic,0)
        for i in range(n):
            dfs(0,i,pacific,0)
            dfs(m-1,i,atlantic,0)

        return list(pacific.intersection(atlantic))