"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        copies = {}
        q = collections.deque()
        q.append(node)
        while q:
            old = q.popleft()
            if old in copies:
                continue
            copies[old] = Node(old.val)
            for neigh in old.neighbors:
                if neigh not in copies:
                    q.append(neigh)
                else:
                    copies[old].neighbors.append(copies[neigh])
                    copies[neigh].neighbors.append(copies[old])
            
        return copies[node]