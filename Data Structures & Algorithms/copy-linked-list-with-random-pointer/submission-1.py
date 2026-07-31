"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copies = {None:None}

        cur = head
        while cur:
            if cur not in copies:
                copies[cur] = Node(cur.val)
            if cur.random not in copies:
                copies[cur.random] = Node(cur.random.val)
            if cur.next not in copies:
                copies[cur.next] = Node(cur.next.val)

            copies[cur].next = copies[cur.next]
            copies[cur].random = copies[cur.random]
            cur = cur.next

        return copies[head]
