class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + '.' + s
        return res
    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != '.':
                j += 1
            wordlen = int(s[i:j])
            res.append(s[j+1:j+wordlen+1])
            print(s[j+1:j+wordlen+1])
            i = j+wordlen+1
        return res