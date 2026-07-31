class Solution:
    def numDecodings(self, s: str) -> int:
        
        n = len(s)
        dp = [0] * (n+1)
        dp[-1] = 1
        if s[-1] != "0":
            dp[-2] = 1
        for i in range(n-2, -1 ,-1):
            if s[i] == "0":
                dp[i] = 0
                continue
            elif s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456"):
                dp[i] += dp[i+2]
            dp[i] += dp[i+1]

        return dp[0]