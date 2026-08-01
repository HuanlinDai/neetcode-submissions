class node:
    def __init__(self, val = None):
        self.val = val
        self.next = None
        
class LinkedList:
    
    def __init__(self):
        self.head = node()
        self.tail = self.head
    
    def get(self, index: int) -> int:
        cur = self.head.next
        for i in range(index):
            if not cur:
                return -1
            cur = cur.next
        if cur:
            return cur.val
        else:
            return -1


    def insertHead(self, val: int) -> None:
        newhead = node(val)
        newhead.next = self.head.next
        self.head.next = newhead
        if not newhead.next:
            self.tail = newhead


    def insertTail(self, val: int) -> None:
        self.tail.next = node(val)
        self.tail = self.tail.next


    def remove(self, index: int) -> bool:
        cur = self.head
        for i in range(index):
            if not cur:
                return False
            cur = cur.next
        if not cur or not cur.next:
            return False
        if self.tail == cur.next:
            self.tail = cur
        cur.next = cur.next.next
        return True

    def getValues(self) -> List[int]:
        res = []
        cur = self.head.next
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res