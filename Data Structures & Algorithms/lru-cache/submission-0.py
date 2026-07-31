class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
        self.cache = {}
        self.cap = capacity

    def remove(self, key):
        if key in self.cache:
            node = self.cache[key]
            l, r = node.prev, node.next
            l.next, r.prev = r, l
            del self.cache[key]
        return None
        
    def insert(self, key, val):
        l, r = self.right.prev, self.right
        new = Node(key,val)
        l.next = new
        r.prev = new
        new.prev = l
        new.next = r
        self.cache[key] = new
        return None

    def get(self, key: int) -> int:
        node = self.cache.get(key,None)
        if not node:
            return -1
        val = node.val
        self.remove(key)
        self.insert(key, val)
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(key)
        self.insert(key, value)
        if len(self.cache) > self.cap:
            todelete = self.left.next
            self.remove(todelete.key)
        return None