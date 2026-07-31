class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        

        longest = ""

        for i in range(len(s)):
            erad = orad = 0
            while 0 <= (i-orad) <= i+orad < len(s):
                cur = s[i-orad:i + orad + 1]
                if cur == cur[::-1]:
                    if len(cur) > len(longest):
                        longest = cur
                else:
                    break
                orad += 1
            while 0 <= (i-erad) <= i+1+erad < len(s):
                cur = s[i-erad:i + erad + 2]
                if cur == cur[::-1]:
                    if len(cur) > len(longest):
                        longest = cur
                else:
                    break
                erad += 1
        return longest