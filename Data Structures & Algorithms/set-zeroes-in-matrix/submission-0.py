class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        rows = set({})
        cols = set({})
        m, n = len(matrix), len(matrix[0])
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    rows.add(row)
                    cols.add(col)
        
        for row in rows:
            matrix[row] = [0] * n
        for col in cols:
            for row in range(m):
                matrix[row][col] = 0
        return None