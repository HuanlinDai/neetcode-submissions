class PrefixTree:

    def __init__(self, val = None):
        self.val = val
        self.word = False
        self.children = {}

    def insert(self, word: str) -> None:
        cur = self
        for i in range(len(word)):
            if word[i] not in cur.children:
                cur.children[word[i]] = PrefixTree(word[i])
            cur = cur.children[word[i]]
        cur.word = True

    def search(self, word: str) -> bool:
        cur = self
        for i in range(len(word)):
            if word[i] not in cur.children:
                return False
            cur = cur.children[word[i]]
        return cur.word

    def startsWith(self, prefix: str) -> bool:
        cur = self
        for i in range(len(prefix)):
            if prefix[i] not in cur.children:
                return False
            cur = cur.children[prefix[i]]
        return True
        