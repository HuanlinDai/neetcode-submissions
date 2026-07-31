class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        s = s.lower()
        letters = set('abcdefghijklmnopqrstuvwxyz1234567890')
        while i <= j:
            if s[i] not in letters:
                i += 1
                continue
            elif s[j] not in letters:
                j -= 1
                continue
            else:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
        return True