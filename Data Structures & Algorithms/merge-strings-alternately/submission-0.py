class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        m, n = len(word1), len(word2)
        for i in range(min(m,n)):
            res += word1[i]
            res += word2[i]
        if m > n:
            res += word1[n:]
        elif n > m:
            res += word2[m:]
        return res