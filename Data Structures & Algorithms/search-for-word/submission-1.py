class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        self.path = set()
        
        def dfs(s, row, col):
            if (row,col) in self.path or not (0<=row<m and 0<=col<n):
                return False
            if s[0] != board[row][col]:
                return False

            self.path.add((row,col))
            if len(s) == 1:
                res = s[0] == board[row][col]
            else:
                res = dfs(s[1:], row-1, col) or \
                    dfs(s[1:], row+1, col) or \
                    dfs(s[1:], row, col-1) or \
                    dfs(s[1:], row, col+1)
            self.path.remove((row,col))
            return res

        for row in range(m):
            for col in range(n):
                if dfs(word, row, col):
                    return True

        return False
