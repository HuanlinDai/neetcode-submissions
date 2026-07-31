class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = set({-1})
        words = set(wordDict)
        for i in range(len(s)):
            for ispace in dp:
                if s[ispace+1:i+1] in words:
                    dp.add(i)
                    break
        return len(s)-1 in dp
