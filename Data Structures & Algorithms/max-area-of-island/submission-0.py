class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        res = 0

        m, n = len(grid), len(grid[0])

        def dfs(i,j):
            if not (0<=i<m and 0<=j<n):
                return 0
            if grid[i][j] == 0:
                return 0
            area = 1
            grid[i][j] = 0
            area += dfs(i+1,j) + dfs(i-1,j) + dfs(i,j+1) + dfs(i,j-1)
            return area

        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i,j))
            

        return res