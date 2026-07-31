class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            a = "".join(sorted(s))
            anagrams[a] = anagrams.get(a, []) + [s]
        res = []
        for a in anagrams:
            res.append(anagrams[a])
        return res