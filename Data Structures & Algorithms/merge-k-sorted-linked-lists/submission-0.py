# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        while lists:
            newlist = lists.pop(0)
            dummy.next = self.mergeLists(dummy.next, newlist)
        return dummy.next


    def mergeLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
        
        cur = dummy = ListNode()
        cur1 = list1
        cur2 = list2
        while cur1 and cur2:
            if cur1.val < cur2.val:
                cur.next = cur1
                cur1 = cur1.next
            else:
                cur.next = cur2
                cur2 = cur2.next
            cur = cur.next

        if not cur1:
            cur.next = cur2
        else:
            cur.next = cur1
        return dummy.next
