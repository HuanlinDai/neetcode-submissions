class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[-1] = True

        for i in range(n-1, -1, -1):
            for word in wordDict:
                if len(word) + i > n:
                    continue
                if dp[len(word) + i] and s[i:i+len(word)] == word:
                    dp[i] = True

        print(dp)
        return dp[0]

