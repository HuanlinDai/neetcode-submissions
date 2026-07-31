class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = l = 0
        freqs = {}
        for r in range(len(s)):
            if s[r] not in freqs:
                freqs[s[r]] = 1
            else:
                freqs[s[r]] += 1

            count = max(freqs.values())
            print(freqs)
            print(count)
            while (r - l + 1) - count > k:
                freqs[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res