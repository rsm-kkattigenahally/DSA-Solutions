# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max = -float("inf")
        self.total = 0
        def dfs(root):
            if not root : return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.total = left+right+root.val
            self.max = max(self.max, self.total, root.val, left+root.val, right+root.val)
            return max(left+root.val,right+root.val, root.val)
        dfs(root)
        return self.max