class Solution:

    def encode(self, strs: List[str]) -> str:
        for i in range(len(strs)):
            slen = len(strs[i])
            strs[i] = str(slen) + '.' + strs[i]
        return "".join(strs)
    def decode(self, s: str) -> List[str]:
        i = 0
        slen = 0
        res = []
        while i < len(s):
            slen = ""
            while s[i] != ".":
                slen += s[i]
                i += 1
            slen = int(slen)
            i += 1
            res.append(s[i:i+slen])
            i += slen
        return res