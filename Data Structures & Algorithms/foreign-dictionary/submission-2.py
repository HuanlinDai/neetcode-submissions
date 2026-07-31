class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        children = {}
        letters = {c for word in words for c in word}
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            l1 = len(word1)
            l2 = len(word2)
            if l1 > l2 and word2 == word1[:l2]:
                return ""
            for j in range(min(l1,l2)):
                if word1[j] != word2[j]:
                    children[word1[j]]=children.get(word1[j],[]) + [word2[j]]
                    break
            
        res = []
        visited = {}
        def dfs(letter):
            if letter in visited:
                return visited[letter]
            
            visited[letter] = True
            for c in children.get(letter,[]):
                if dfs(c):
                    return True
            visited[letter] = False
            res.append(letter)
            return False

        for c in letters:
            if dfs(c):
                return ""
        return "".join(res[::-1])
        