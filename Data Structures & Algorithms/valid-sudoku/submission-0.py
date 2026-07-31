class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def check(l):
            seen = set({})
            for c in l:
                if c == ".":
                    continue
                if c in seen:
                    return False
                seen.add(c)
            return True

        for row in range(9):
            if not check(board[row]):
                return False
        for col in range(9):
            l = []
            for row in range(9):
                l.append(board[row][col])
            if not check(l):
                return False
        for i in range(3):
            for j in range(3):
                l = board[3*i][3*j:3*j+3] + board[3*i+1][3*j:3*j+3] + board[3*i+2][3*j:3*j+3]
                if not check(l):
                    return False
        return True
        