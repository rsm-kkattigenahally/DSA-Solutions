# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        dummy = head
        while head:
            count+=1
            head = head.next
        
        remove = count - n
        count = 0
        head = dummy
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        while count<remove:
            prev = head
            head = head.next
            count+=1
        prev.next = head.next
        head = prev
        return dummy.next


