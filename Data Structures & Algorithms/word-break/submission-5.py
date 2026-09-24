class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}
        words = set(wordDict)
        n = len(s)
        def dfs(start) -> bool:
            if start >= n:
                return True
            if start in dp:
                return dp[start]
            for i in range(start, n+1):
                if s[start:i] in words:
                    dp[i] = dfs(i)
                    if dp[i]:
                        return True
            dp[i] = False
            return False
            
        return dfs(0)