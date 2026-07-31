# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head:
            return None

        kfinder = head
        zerofinder = head
        dummy = tail = ListNode()
        nextstart = head.next

        prev = head.next
        cur = head
        next = head.next

        counter = 0
        while nextstart:
            counter += 1
            if counter == k:
                # reverse
                while cur != kfinder:
                    cur.next = prev
                    prev = cur
                    cur = next
                    next = next.next
                cur.next = prev
                # attach kfinder as new head
                tail.next = kfinder
                # reset counter
                counter = 0
                tail = zerofinder
                zerofinder = nextstart
                cur = nextstart
                next = nextstart.next
            kfinder = nextstart
            nextstart = nextstart.next
            prev = nextstart
        if kfinder and counter +1 == k:
            
            # reverse
            while cur != kfinder:
                cur.next = prev
                prev = cur
                cur = next
                next = next.next
            cur.next = prev
            # attach kfinder as new head
            tail.next = kfinder 
        return dummy.next

            

