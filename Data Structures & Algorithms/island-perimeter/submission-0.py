class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        self.visited = set()
        self.res = 0
        self.m, self.n = len(grid), len(grid[0])
        def dfs(i,j):
            if (i,j) in self.visited:
                return 0
            if not (0<=i<self.m and 0<=j<self.n):
                return 1
            if grid[i][j] == 0:
                return 1

            self.visited.add((i,j))
            numedges = dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1)
            self.res += numedges
            return 0

        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 1:
                    dfs(i,j)
                    return self.res