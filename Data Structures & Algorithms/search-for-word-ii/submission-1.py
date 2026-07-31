class TrieNode:
    def __init__(self):
        self.word = ''
        self.children = {}
    def add(self, word):
        cur = self
        for i in range(len(word)):
            if word[i] not in cur.children:
                cur.children[word[i]] = TrieNode()
            cur = cur.children[word[i]]
        cur.word = word
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = TrieNode()
        res = set({})
        for word in words:
            trie.add(word)
        
        
        def dfs(node, i, j):
            if not (0<=i<m and 0<=j<n) or (i,j) in path or len(words) == len(res):
                return None
            if (board[i][j] in node.children):
                path.add((i,j))
                child = node.children[board[i][j]]
                if child.word:
                    res.add(child.word)
                dfs(child, i+1, j)
                dfs(child, i-1, j)
                dfs(child, i, j+1)
                dfs(child, i, j-1)
                path.remove((i,j))
            return None
            
        path = set({})
        m, n = len(board), len(board[0])
        for row in range(m):
            for col in range(n):
                dfs(trie, row, col)
        return list(res)