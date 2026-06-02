class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # for a graph to be a tree there : if there aree n node, there should be exactly n-1 edges
        # edges > n-1 there is a cycle
        # we return the last edge in the input that forms a cycle
        parent = [i for i in range(0,len(edges)+1)]
        rank = [1]*(len(edges)+1)
        def find(x):
            while parent[x]!=x:
                x = parent[x]
            return x
        
        def union(x,y):
            px, py = find(x), find(y)
            if px==py: return [x,y]
            if rank[px]>=rank[py]:
                rank[px]+=rank[py]
                parent[py] = px
            else :
                rank[py]+=rank[px]
                parent[px] = py
            return 
        
        for e in edges:
            un = union(e[0],e[1])
            if un is not None:
                return un