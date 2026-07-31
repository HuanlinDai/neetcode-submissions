class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = -1
        s1freqs = {}
        for c in s1:
            s1freqs[c] = s1freqs.get(c,0) + 1
        
        s2freqs = {}
        for r in range(len(s2)):
            s2freqs[s2[r]] = s2freqs.get(s2[r], 0) + 1
            if s2freqs[s2[r]] > s1freqs.get(s2[r],0):
                while l < r:
                    l += 1
                    s2freqs[s2[l]] -= 1
                    if s2[l] == s2[r]:
                        break                
            elif s2freqs[s2[r]] == s1freqs[s2[r]]:
                done = True
                for c in s1freqs:
                    if s1freqs[c] != s2freqs.get(c,0):
                        done = False
                        break
                if done:
                    return True
                
        return False