class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sfreqs = Counter(s)
        tfreqs = Counter(t)
        for c in sfreqs:
            if tfreqs.get(c,0) != sfreqs[c]:
                return False
        for c in tfreqs:
            if sfreqs.get(c,0) != tfreqs[c]:
                return False
        return True