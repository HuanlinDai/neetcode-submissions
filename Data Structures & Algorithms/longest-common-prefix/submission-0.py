class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        minlength = len(min(strs, key = len))
        for ind in range(minlength):
            c = strs[0][ind]
            for s in strs:
                if s[ind] != c:
                    return res
            res += c
        return res