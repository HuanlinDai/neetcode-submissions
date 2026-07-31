class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        path = set({}) 
        def dfs(ind, row, col):
            if ind == len(word):
                return True
            if not (0 <= row < m and 0 <= col < n) or (row, col) in path or word[ind] != board[row][col]:
                return False
            path.add((row, col))

            truth = (dfs(ind + 1, row - 1, col) or
                    dfs(ind+1, row+1, col) or
                    dfs(ind+1, row, col-1) or
                    dfs(ind+1, row, col+1))
            path.remove((row, col))
            return truth

        for row in range(m):
            for col in range(n):
                if board[row][col] == word[0]:
                    if dfs(0, row, col):
                        return True
        return False
