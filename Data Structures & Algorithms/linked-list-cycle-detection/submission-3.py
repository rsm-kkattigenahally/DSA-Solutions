# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head
        while fast and fast.next :   # we need to check only fast because it will always be ahead when there is no loop
            fast = fast.next.next
            slow = slow.next
            if fast==slow: return True
        return False
