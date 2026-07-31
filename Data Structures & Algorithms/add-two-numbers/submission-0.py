# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        total = 0
        cur1 = l1
        cur2 = l2
        carry = 0
        head = ListNode()
        cur = head
        while cur1 or cur2 or carry:
            cur.next = ListNode()
            if cur1:
                cur.next.val += cur1.val
                cur1 = cur1.next
            if cur2:
                cur.next.val += cur2.val
                cur2 = cur2.next
            if carry:
                cur.next.val += carry
            if cur.next.val >= 10:
                carry = 1
                cur.next.val -= 10
            else:
                carry = 0
            cur = cur.next



        return head.next