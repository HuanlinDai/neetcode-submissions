class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        m = len(board)
        n = len(board[0])
        p = len(word)
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        stack = set()
        def dfs(i,j,k) -> bool:
            if board[i][j] == word[k] and (i,j) not in stack:
                if k == p-1:
                    return True
                stack.add((i,j))
                for diri, dirj in dirs:
                    if 0<=i+diri<m and 0<=j+dirj<n and dfs(i+diri,j+dirj,k+1):
                        return True
                stack.remove((i,j))
            return False
            
        
        for i in range(m):
            for j in range(n):
                if dfs(i,j,0):
                    return True
        return False