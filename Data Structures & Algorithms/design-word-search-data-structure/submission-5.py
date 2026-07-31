class WordDictionary:

    def __init__(self, val = None):
        self.val = val
        self.word = False
        self.children = {}

    def addWord(self, word: str) -> None:
        cur = self
        for i in range(len(word)):
            if word[i] not in cur.children:
                cur.children[word[i]] = WordDictionary(word[i])
            cur = cur.children[word[i]]
        cur.word = True
        print(f"{cur.val} {cur.word}")
        return None

    def search(self, word: str) -> bool:
        curq = [self]
        nextq = []
        for i in range(len(word)):
            print(f'searching for {word[i]}')
            if not curq:
                print("curq empty")
                return False
            for node in curq:
                if word[i] == '.':
                    nextq += node.children.values()
                else:
                    child = node.children.get(word[i], None)
                    if child:
                        nextq.append(child)

            curq = nextq
            nextq = []
        
        for node in curq:
            print(node.val)
            if node.word:
                return True
        return False