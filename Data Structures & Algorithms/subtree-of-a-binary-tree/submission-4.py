class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        
        def dfs(root, subroot):
            if not root and not subroot:
                return True
            if not root or not subroot: return False
            if root.val !=subroot.val: return False
           
            l = dfs(root.left, subroot.left)
            r = dfs(root.right, subroot.right)
            return l and r
        
        def find(root):
            if not root: return False
            res = False
            if root.val == subroot.val:
                res = dfs(root,subroot)
            return res or find(root.left) or find(root.right)
        
        
        r = find(root)
        if r is None: return False
        return r