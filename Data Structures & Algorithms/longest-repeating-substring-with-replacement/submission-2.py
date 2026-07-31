class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = l = maxf = 0
        freqs = {}
        for r in range(len(s)):
            freqs[s[r]] = freqs.get(s[r],0) + 1
            maxf = max(maxf, freqs[s[r]])
            while (r - l + 1) - maxf > k:
                freqs[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res