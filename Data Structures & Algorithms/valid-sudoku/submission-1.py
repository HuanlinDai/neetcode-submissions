class Solution:
    def validRow(self, row: List[str]) -> bool:
        elements = set()
        for e in row:
            if e != '.' and e in elements:
                return False
            elements.add(e)
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            if not self.validRow(board[i]):
                return False
            if not self.validRow([board[j][i] for j in range(9)]):
                return False
            row, col = i//3, i%3
            if not self.validRow(board[row*3][col*3:col*3+3] + board[row*3 + 1][col*3:col*3+3] + board[row*3 + 2][col*3:col*3+3]):
                return False

        return True