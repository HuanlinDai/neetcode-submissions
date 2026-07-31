class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        letters = ('qwertyuiopasdfghjklzxcvbnm1234567890')
        i = 0
        j = len(s)-1
        while i < j:
            if s[i] not in letters:
                i += 1
                continue
            if s[j] not in letters:
                j -= 1
                continue
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
