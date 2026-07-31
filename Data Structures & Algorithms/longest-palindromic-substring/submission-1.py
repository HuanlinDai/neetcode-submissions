class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n = len(s)
        longest = ''
        for i in range(n):
            orad = erad = 0
            while 0 <= i - orad and i + orad < n:
                if s[i-orad:i+orad+1] == s[i-orad:i+orad+1][::-1]:
                    if len(longest) < 1 + orad * 2:
                        longest = s[i-orad:i+orad+1]
                else:
                    break
                orad += 1
                
            while 0 <= i - erad and i + 1 + erad < n:
                if s[i - erad:i+erad+2] == s[i - erad:i+erad+2][::-1]:
                    if len(longest) < (1 + erad) * 2:
                        longest = s[i - erad:i+erad+2]
                else:
                    break
                erad += 1

        return longest