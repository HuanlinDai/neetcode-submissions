# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        listlen = 0
        cur = head
        while cur:
            cur = cur.next
            listlen += 1

        cur = head
        prev = None
        i = 0
        while i < listlen-n:
            prev = cur
            cur = cur.next
            i += 1
        if prev == None or cur == None:
            return head.next
        
        prev.next = cur.next
        return head