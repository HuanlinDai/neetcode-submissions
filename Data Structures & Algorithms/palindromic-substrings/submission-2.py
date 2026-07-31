class Solution:
    def countSubstrings(self, s: str) -> int:
        self.res = 0
        for i in range(len(s)-1):
            self.checkPali(s, i, i)
            self.checkPali(s, i, i+1)
        return self.res + 1

        
    def checkPali(self, s, l, r):
        rad = 0
        while 0 <= l - rad and r + rad < len(s) and s[l-rad:r+rad+1] == s[l-rad:r+rad+1][::-1]:
            self.res += 1
            rad +=1

        return