class PrefixTree:

    def __init__(self):
        self.val = False
        self.children = {}

    def insert(self, word: str) -> None:
        if len(word) == 0:
            self.val = True
            return None
        
        c = word[0]
        if c not in self.children:
            self.children[c] = PrefixTree()
        if len(word) == 1:
            self.children[c].insert('')
        else:
            self.children[c].insert(word[1:])
        return None
        

    def search(self, word: str) -> bool:
        if len(word) == 0:
            return self.val

        if word[0] not in self.children:
            return False
        
        return self.children[word[0]].search(word[1:])

    def startsWith(self, prefix: str) -> bool:
        if len(prefix) == 0:
            return True

        if prefix[0] not in self.children:
            return False
        
        return self.children[prefix[0]].startsWith(prefix[1:])
        