class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tfreqs = {}
        for c in t:
            tfreqs[c] = tfreqs.get(c,0) + 1
        sfreqs = {}

        res = s + " "
        n = len(s)
        l = 0
        for r in range(n):
            sfreqs[s[r]] = sfreqs.get(s[r],0) + 1
            if sfreqs[s[r]] >= tfreqs.get(s[r],0):
                # check that tfreqs is contained
                contained = True
                for c in tfreqs:
                    if tfreqs[c] > sfreqs.get(c,0):
                        contained = False
                        break
                if not contained:
                    # print(f"{s[l:r+1]} doesn't contain")
                    continue
                while l <= r:
                    # print(f"{s[l:r+1]} contains")
                    if r+1-l < len(res):
                        res = s[l:r+1]
                    sfreqs[s[l]] -= 1
                    if sfreqs[s[l]] < tfreqs.get(s[l],0):
                        l+=1
                        break
                    l += 1
                
            else:
                continue
        if res == s + " ":
            return ""
        return res
            