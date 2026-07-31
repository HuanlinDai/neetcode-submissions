class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        dp = [[False] * (n+1) for _ in range(m+1)]
        dp[m][n] = True

        for row in range(m,-1,-1):
            for col in range(n,-1,-1):
                if row < m and s1[row] == s3[row+col] and dp[row+1][col]:
                    dp[row][col] = True
                if col < n and s2[col] == s3[row+col] and dp[row][col+1]:
                    dp[row][col] = True

        
        return dp[0][0]