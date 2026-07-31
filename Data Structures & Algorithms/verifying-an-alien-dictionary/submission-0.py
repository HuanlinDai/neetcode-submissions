class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        inds = {}
        for i in range(len(order)):
            inds[order[i]] = i
        
        n = len(words)
        for i in range(n-1):
            word1 = words[i]
            word2 = words[i+1]
            passed = False
            for k in range(min(len(word1), len(word2))):
                if inds[word1[k]] < inds[word2[k]]:
                    passed = True
                    break
                elif inds[word1[k]] > inds[word2[k]]:
                    return False
            if passed:
                continue
            if len(word1) > len(word2):
                return False

        return True

