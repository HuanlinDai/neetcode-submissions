class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        m, n = len(s), len(p)
        dp = {}
        def dfs(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            if j >= n:
                return i >= m
            
            match = i < m and (s[i] == p[j] or p[j] == ".")
            if j < n-1 and p[j+1] == "*":
                dp[(i,j)] = dfs(i, j+2) or (match and dfs(i+1,j))
            elif match:
                dp[(i,j)] = dfs(i+1, j+1)
            else:
                dp[(i,j)] = False
            return dp[(i,j)]

        return dfs(0,0)