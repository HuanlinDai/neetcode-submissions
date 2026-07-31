class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        m, n = len(s), len(t)
        dp = {}

        def dfs(i,j):

            if j == n:
                return 1
            elif i == m:
                return 0
            elif (i,j) in dp:
                return dp[(i,j)]

            res = dfs(i+1,j)
            if s[i] == t[j]:
                res += dfs(i+1,j+1)
            return res
        return dfs(0,0)