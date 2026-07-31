class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sfreqs = {}
        tfreqs = {}
        for c in s:
            sfreqs[c] = sfreqs.get(c, 0) + 1
        for c in t:
            tfreqs[c] = tfreqs.get(c, 0) + 1
        for c in sfreqs:
            if tfreqs.get(c,0) != sfreqs[c]:
                return False
        for c in tfreqs:
            if sfreqs.get(c,0) != tfreqs[c]:
                return False
        return True