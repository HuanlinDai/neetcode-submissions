class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0
        n = len(s)
        for i in range(n-1):
            res += abs(ord(s[i]) - ord(s[i+1]))
        return res