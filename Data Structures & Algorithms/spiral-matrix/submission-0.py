class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rowstart = colstart = 0
        rowend, colend = len(matrix), len(matrix[0])
        res = []
        while rowstart < rowend and colstart < colend:
            for col in range(colstart, colend):
                res.append(matrix[rowstart][col])
            for row in range(rowstart+1, rowend):
                res.append(matrix[row][colend-1])
            if rowend-rowstart > 1 and colend-colstart > 1:
                for col in range(colend-2, colstart-1,-1):
                    res.append(matrix[rowend-1][col])
                for row in range(rowend-2,rowstart, -1):
                    res.append(matrix[row][colstart])
            rowstart += 1
            rowend -= 1
            colstart += 1
            colend -= 1
        return res