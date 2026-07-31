class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        i = 0
        for j in range(n):
            if i == m:
                return True
            if t[j] == s[i]:
                i += 1
        return i == m