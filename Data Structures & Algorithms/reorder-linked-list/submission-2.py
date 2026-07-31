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

        list2 = head
        for _ in range(n//2):
            list2 = list2.next

        prev = None
        next = list2.next
        while next:
            list2.next = prev
            prev = list2
            list2 = next
            next = next.next
        list2.next = prev
        list1 = head

        next1 = head.next
        next2 = list2.next
        while next1 and next2:
            list1.next = list2
            list2.next = next1

            list1 = next1
            list2 = next2
            next1 = next1.next
            next2 = next2.next

        return None
