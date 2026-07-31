# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
        if n <= 2:
            return None
        mid = (n+1)//2
        cur = head
        while mid > 0:
            cur = cur.next
            mid -= 1
        
        prev = None
        nextnode = cur.next
        while nextnode:
            cur.next = prev
            prev = cur
            cur = nextnode
            nextnode = nextnode.next
        cur.next = prev
        newhead = cur

        cur1 = head
        cur2 = newhead
        next1 = cur1
        next2 = cur2

        while cur1 and cur2:
            next1 = cur1.next
            next2 = cur2.next
            cur1.next = cur2
            cur2.next = next1
            cur1 = next1
            cur2 = next2
            
            
        if cur1:
            cur1.next = None
