class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rotten = []

        m, n = len(grid), len(grid[0])
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 2:
                    rotten.append((row,col,0))

        q = []
        res = 0
        while rotten:
            row, col, t = rotten.pop(0)
            res = max(res, t)
            if 0 < row and grid[row-1][col] == 1:
                rotten.append((row-1,col,t + 1))
                grid[row-1][col] = 0
            if 0 < col and grid[row][col-1] == 1:
                rotten.append((row,col-1,t + 1))
                grid[row][col-1] = 0
            if row < m - 1 and grid[row+1][col] == 1:
                rotten.append((row+1,col,t + 1))
                grid[row+1][col] = 0
            if col < n - 1 and grid[row][col+1] == 1:
                rotten.append((row,col+1,t + 1))
                grid[row][col+1] = 0

            grid[row][col] = 0

        m, n = len(grid), len(grid[0])
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    return -1

        return res

        