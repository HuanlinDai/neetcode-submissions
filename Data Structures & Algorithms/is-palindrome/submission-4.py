class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        while i < j:
            if not (ord('A') <= ord(s[i]) <= ord('Z') or ord('a') <= ord(s[i]) <= ord('z') or ord('0') <= ord(s[i]) <= ord('9')):
                i += 1
                continue
            elif not (ord('A') <= ord(s[j]) <= ord('Z') or ord('a') <= ord(s[j]) <= ord('z') or ord('0') <= ord(s[j]) <= ord('9')):
                j -= 1
                continue
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True