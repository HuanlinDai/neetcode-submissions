# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        
        dummy = ListNode(next = head)

        cur = head
        numnodes = 0
        while cur:
            cur = cur.next
            numnodes += 1
        
        skip = numnodes - n

        cur = dummy
        for _ in range(skip):
            cur = cur.next
        cur.next = cur.next.next

        return dummy.next