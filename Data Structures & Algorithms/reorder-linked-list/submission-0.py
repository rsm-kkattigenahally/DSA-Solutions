class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # collect all values
        vals = []
        cur = head
        while cur:
            vals.append(cur.val)
            cur = cur.next
        
        # two pointer reorder in place
        l, r = 0, len(vals) - 1
        cur = head
        while l <= r:
            cur.val = vals[l]
            cur = cur.next
            l += 1
            if l <= r:
                cur.val = vals[r]
                cur = cur.next
                r -= 1