# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([root])
        newq = deque([])
        if not root: return []
        ans = [[root.val]]
        level = []
        while q:
            for n in q:
                if n.left:
                    newq.append(n.left)
                    level.append(n.left.val)
                if n.right:
                    newq.append(n.right)
                    level.append(n.right.val)
            if level != []:
                ans.append(level)
            level = []
            q = newq.copy()
            newq = deque([])

        return ans
            

