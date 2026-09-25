# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        h = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(h, (lists[i].val, i))
        cur = dummy
        while h:
            _, i = heapq.heappop(h)
            cur.next = lists[i]
            lists[i] = lists[i].next
            if lists[i]:
                heapq.heappush(h, (lists[i].val,i))
            cur = cur.next
        return dummy.next