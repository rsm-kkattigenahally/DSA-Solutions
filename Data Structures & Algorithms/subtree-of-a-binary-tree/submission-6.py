class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        
        def sametree(root, subroot):
            if not root and not subroot: return True
            if not root or not subroot: return False
            if root.val != subroot.val: return False
            l = sametree(root.left, subroot.left)
            r = sametree(root.right, subroot.right)
            return l and r
        
        def find(root, subroot):
            if not root: return False
            res = False
            if root.val == subroot.val:
                res = sametree(root, subroot)
            l = find(root.left, subroot)
            r = find(root.right, subroot)
            return res or l or r
        
        return find(root, subroot)

    
