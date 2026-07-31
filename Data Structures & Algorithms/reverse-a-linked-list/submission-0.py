# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        prev = None
        cur = head
        nextnode = head.next
        while nextnode:
            cur.next = prev
            prev = cur
            cur = nextnode
            nextnode = nextnode.next
        cur.next = prev
        return cur