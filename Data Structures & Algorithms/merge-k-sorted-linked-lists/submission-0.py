# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for l in lists:
            head = l
            while head:
                heapq.heappush(heap, head.val)
                head = head.next
        dummy = ListNode()
        h = dummy
        if not heapq:
            return dummy
        while heap:
            h.next = ListNode(heapq.heappop(heap))
            h = h.next
        
        return dummy.next
