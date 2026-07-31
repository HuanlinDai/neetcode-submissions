class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        q = collections.deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i,j,0))

        while q:
            i,j,dist = q.popleft()
            grid[i][j] = min(grid[i][j],dist)
            if i > 0 and grid[i-1][j] == 2147483647:
                q.append((i-1,j,dist+1))
            if i < m-1 and grid[i+1][j] == 2147483647:
                q.append((i+1,j,dist+1))
            if j > 0 and grid[i][j-1] == 2147483647:
                q.append((i,j-1,dist+1))
            if j < n-1 and grid[i][j+1] == 2147483647:
                q.append((i,j+1,dist+1))
            
            
        return None