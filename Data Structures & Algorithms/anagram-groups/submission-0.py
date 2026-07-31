class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s not in anagrams:
                anagrams[sorted_s] = [s]
            else:
                anagrams[sorted_s].append(s)
        res = []
        for s in anagrams:
            res.append(anagrams[s])
        return res