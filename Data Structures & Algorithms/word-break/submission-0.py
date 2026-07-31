class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = set({-1})
        words = set(wordDict)
        for i in range(len(s)):
            newdp = set({})
            for ispace in dp:
                if s[ispace+1:i+1] in words:
                    newdp.add(i)
            dp = dp.union(newdp)
        return len(s)-1 in dp
