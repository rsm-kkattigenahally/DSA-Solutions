# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        ans = []
        q = deque([])
        q.append(root)
        newq = deque()
        while q:
            print(q)
            for n in q:
                node = n
                if n.left:
                    newq.append(n.left)
                if n.right:
                    newq.append(n.right)
            ans.append(node.val)
            q = deque()
            q = q + newq
            newq = deque()
        return ans
        
