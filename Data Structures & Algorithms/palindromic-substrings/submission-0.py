class Solution:
    def countSubstrings(self, s: str) -> int:
        
        n = len(s)
        res = 0
        for i in range(n):
            orad = erad = 0

            while 0<=i-orad and i+orad<n:
                if s[i-orad:i+orad+1] == s[i-orad:i+orad+1][::-1]:
                    res += 1
                else:
                    break
                orad += 1
                
            while 0<=i-erad and i+erad+1<n:
                if s[i-erad:i+erad+2] == s[i-erad:i+erad+2][::-1]:
                    res += 1
                else:
                    break
                erad += 1
        return res