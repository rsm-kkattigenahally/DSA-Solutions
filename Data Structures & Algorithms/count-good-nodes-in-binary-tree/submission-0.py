# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        self.prev = None
        maxval = root.val
        def dfs(root, maxval):
            if not root:return
            if root.val>=maxval:
                self.count+=1
            maxval = max(maxval, root.val)
            l = dfs(root.left, maxval)
            r = dfs(root.right, maxval)
        dfs(root, maxval)
        return self.count