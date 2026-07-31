class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.m, self.n = len(grid), len(grid[0])
        
        def dfs(row,col):
            if not (0<=row<self.m) or not (0<=col<self.n):
                return 0
            if grid[row][col] == "1":
                grid[row][col] = "0"
                dfs(row-1,col)
                dfs(row+1,col)
                dfs(row,col-1)
                dfs(row,col+1)
                return 1
            else:
                return 0
        res = 0
        for row in range(self.m):
            for col in range(self.n):
                res += dfs(row,col)

        return res