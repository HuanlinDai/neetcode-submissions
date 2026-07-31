class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        m, n = len(heights), len(heights[0])
        pacific = set({})
        atlantic = set({})

        def dfs(row, col, ocean, prevHeight):
            if not (0<=row<m and 0<=col<n) or (row,col) in ocean or heights[row][col] < prevHeight:
                return
            ocean.add((row,col))
            dfs(row+1,col,ocean,heights[row][col])
            dfs(row-1,col,ocean,heights[row][col])
            dfs(row,col+1,ocean,heights[row][col])
            dfs(row,col-1,ocean,heights[row][col])
            return


        for c in range(n):
            dfs(0,c,pacific,heights[0][c])
            dfs(m-1,c,atlantic,heights[m-1][c])
        for r in range(m):
            dfs(r,0,pacific,heights[r][0])
            dfs(r,n-1,atlantic,heights[r][n-1])
            
        return list(atlantic.intersection(pacific))