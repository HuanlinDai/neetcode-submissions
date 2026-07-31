class Solution:
    def longestPalindrome(self, s: str) -> str:
        orad = 0
        erad = 0
        res = ""
        n = len(s)
        for i in range(n):
            while 0 <= i - orad and i + orad < n and s[i-orad:i+orad+1] == s[i-orad:i+orad+1][::-1]:
                if 2*orad + 1 > len(res):
                    res = s[i-orad:i+orad+1]
                orad += 1
            while 0 <= i - erad and i + erad + 1 < n and s[i-erad:i+erad+2] == s[i-erad:i+erad+2][::-1]:
                if 2*(erad+1) > len(res):
                    res = s[i-erad:i+erad+2]
                erad += 1

        return res