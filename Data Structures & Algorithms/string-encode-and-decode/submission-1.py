class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append(".")
            res.append(s)
        return "".join(res)
    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        last = 0
        while i < len(s):
            while s[i] != ".":
                i += 1
            lens = int(s[last:i])
            i += 1
            res.append(s[i:i+lens])
            i = i + lens
            last = i
        return res