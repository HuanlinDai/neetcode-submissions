class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        freqs1 = {}
        for c in s1:
            freqs1[c] = freqs1.get(c, 0) + 1
        freqs2 = {}
        for r in range(len(s2)):
            c2 = s2[r]
            freqs2[c2] = freqs2.get(c2,0) + 1
            while l <= r and freqs2[c2] > freqs1.get(c2, 0):
                freqs2[s2[l]] -= 1
                l += 1
            if r - l + 1 == len(s1):
                return True
        return False