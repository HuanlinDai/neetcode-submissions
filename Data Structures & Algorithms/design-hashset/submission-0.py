class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyHashSet:

    def __init__(self):
        self.bins = [None] * 10000
        self.M = 10000
        for i in range(10000):
            self.bins[i] = Node(-1)

    def add(self, key: int) -> None:
        i = key%self.M
        cur = self.bins[i]
        while cur.next:
            if cur.next.val == key:
                return
            cur = cur.next
        cur.next = Node(key)

    def remove(self, key: int) -> None:
        i = key%self.M
        cur = self.bins[i]
        while cur.next:
            if cur.next.val == key:
                cur.next = cur.next.next
                return
            cur = cur.next
        return
        
    def contains(self, key: int) -> bool:
        i = key%self.M
        cur = self.bins[i]
        while cur.next:
            if cur.next.val == key:
                return True
            cur = cur.next
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)