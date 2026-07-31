class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sfreqs = {}
        tfreqs = {}
        shortest = s + ' '
        for c in t:
            if c not in tfreqs:
                tfreqs[c] = 1
            else:
                tfreqs[c] += 1

        l = r = 0
        while r < len(s):
            enough_cs = True
            if s[r] not in sfreqs:
                sfreqs[s[r]] = 1
            else:
                sfreqs[s[r]] += 1
            
            for c in tfreqs:
                if c not in sfreqs:
                    enough_cs = False
                    break
                elif sfreqs[c] < tfreqs[c]:
                    enough_cs = False
                    break
            if enough_cs:
                if len(shortest) > r - l + 1:
                    shortest = s[l:r+1]
                while l < r:
                    if s[l] not in tfreqs:
                        sfreqs[s[l]] -= 1
                    elif sfreqs[s[l]] - 1 >= tfreqs[s[l]]:
                        sfreqs[s[l]] -= 1
                    else:
                        break
                    l += 1
                    if len(shortest) > r - l + 1:
                        shortest = s[l:r+1]
            r += 1

        if shortest == s + ' ':
            return ""
        return shortest