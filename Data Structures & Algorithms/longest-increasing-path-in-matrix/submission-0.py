class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        dp = {}
        dirs = ((-1,0), (1,0), (0,-1), (0,1))
        m, n = len(matrix), len(matrix[0])
        def dfs(r, c, prev):
            if (r<0 or c<0 or r>=m or c>=n):
                return 0
            elif matrix[r][c] <= prev:
                return 0
            elif (r,c) in dp:
                return dp[(r,c)]

            res = 1
            for rd, cd in dirs:
                res = max(res, 1+dfs(r+rd,c+cd,matrix[r][c]))
            dp[(r,c)] = res
            return res

        res = 1

        for r in range(m):
            for c in range(n):
                res = max(res, dfs(r,c, -1))

        return res

        
                    