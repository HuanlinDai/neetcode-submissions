class Solution:
    def countSubstrings(self, s: str) -> int:
        
        res = 0

        for i in range(len(s)):
            erad = orad = 0
            while 0 <= (i-orad) <= i+orad < len(s):
                cur = s[i-orad:i + orad + 1]
                if cur == cur[::-1]:
                    res += 1
                else:
                    break
                orad += 1
            while 0 <= (i-erad) <= i+1+erad < len(s):
                cur = s[i-erad:i + erad + 2]
                if cur == cur[::-1]:
                    res += 1
                else:
                    break
                erad += 1
        return res