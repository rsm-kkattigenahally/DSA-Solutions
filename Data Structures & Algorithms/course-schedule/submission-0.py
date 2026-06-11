class Solution:
    def canFinish(self, numCourses: int, pre: List[List[int]]) -> bool:
        adj = {x:[] for x in range(numCourses)}
        for u,v in pre:
            adj[v].append(u)
        indeg = [0]*numCourses
        for u,v in pre:
            indeg[u]+=1
        q = deque([x for x in range(numCourses) if indeg[x]==0])
        order = []
        while q:
            node = q.popleft()
            order.append(node)
            for ngbr in adj[node]:
                indeg[ngbr]-=1
                if indeg[ngbr]==0:
                    q.append(ngbr)
                    

        if len(order)==numCourses: return True
        return False
                

