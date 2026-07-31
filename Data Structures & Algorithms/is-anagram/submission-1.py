class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sfreqs = {}
        tfreqs = {}
        for ls in s:
            if ls not in sfreqs:
                sfreqs[ls] = 1
            else:
                sfreqs[ls]+=1
        for lt in t:
            if lt not in tfreqs:
                tfreqs[lt] = 1
            else:
                tfreqs[lt] += 1
        return sfreqs == tfreqs