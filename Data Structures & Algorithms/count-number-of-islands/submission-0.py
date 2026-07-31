class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        island=set({})
        def dfs(row,col):
            if not (0<=row<m and 0<=col<n) or grid[row][col] == "0" or (row, col) in island:
                return False
            island.add((row,col))
            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)
            grid[row][col] = "0"
            island.remove((row,col))
            return True


        for row in range(m):
            for col in range(n):
                if dfs(row, col):
                    res += 1
        return res