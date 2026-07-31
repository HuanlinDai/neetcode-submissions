class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        safe = set()
        m, n = len(board), len(board[0])
        def dfs(i,j):
            if (i,j) in safe or not (0<=i<m and 0<=j<n):
                return
            if board[i][j] == "O":
                safe.add((i,j))
                dfs(i+1,j)
                dfs(i-1,j)
                dfs(i,j+1)
                dfs(i,j-1)
            return
        
        for i in range(m):
            dfs(i,0)
            dfs(i,n-1)
        for i in range(n):
            dfs(0,i)
            dfs(m-1,i)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and (i,j) not in safe:
                    board[i][j] = "X"
        return None