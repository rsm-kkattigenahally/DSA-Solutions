class Solution:
    def lowestCommonAncestor(self, root, p, q):
        def lca(root):
            if not root:
                return None
            if root.val == p.val or root.val == q.val:
                return root
            l = lca(root.left)
            r = lca(root.right)
            if l and r: return root
            return l or r
        return lca(root)

            
