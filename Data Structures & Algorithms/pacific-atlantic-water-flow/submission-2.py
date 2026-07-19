class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])
        pac = [(0,i) for i in range(m)] + [(i,0) for i in range(1,n)]
        atl = [(n-1,i) for i in range(m)] + [(i,m-1) for i in range(n-1)]
        #print(pac, atl)
        def bfs(borders):
            visited = set()
            for bor in borders:
                visited.add(bor)
            q = deque([x for x in borders])
            dirs = [[0,1],[1,0],[0,-1],[-1,0]]
            while q:
                u,v = q.popleft()
                for i,j in dirs:
                    du, dv = i+u, v+j
                    if 0<=du<n and 0<=dv<m and (du,dv) not in visited and heights[du][dv]>=heights[u][v]:
                        visited.add((du,dv))
                        q.append((du,dv))
            return visited
        pacific = bfs(pac)
        atlantic = bfs(atl)
        inter = pacific & atlantic
        res = []
        for i,j in inter:
            res.append([i,j])
        
        return res
