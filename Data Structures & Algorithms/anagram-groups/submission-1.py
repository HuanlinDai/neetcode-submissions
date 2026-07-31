class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            ss = "".join(sorted(s))
            if ss in anagrams:
                anagrams[ss].append(s)
            else:
                anagrams[ss] = [s]
        return list(anagrams.values())