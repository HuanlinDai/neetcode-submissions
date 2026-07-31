class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowl = 0
        rowr = len(matrix) - 1
        while rowl <= rowr:
            rowm = (rowl + rowr)//2
            if matrix[rowm][0] <= target <= matrix[rowm][-1]:
                break
            elif target < matrix[rowm][0]:
                rowr = rowm - 1
            else:
                rowl = rowm + 1
        print
        l = 0
        r = len(matrix[0]) - 1
        row = matrix[rowm]
        while l <= r:
            m = (l + r) // 2
            if row[m] == target:
                return True
            elif row[m] < target:
                l = m + 1
            else:
                r = m - 1
        return False