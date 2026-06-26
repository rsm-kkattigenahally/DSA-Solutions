class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])
        # top row left col
        pacific = [(0,i) for i in range(m)] + [(i,0) for i in range(1,n)]
        #bottom row and right col
        atlantic = [(n-1,i) for i in range(m)] + [(i, m-1) for i in range(0,n-1)]

        # print(pacific, atlantic)
        def bfs(borders):
            visited = set()
            dirs = [[-1,0],[1,0],[0,1],[0,-1]]
            for cell in borders:
                visited.add(cell)
            q = deque([x for x in borders])
            while q:
                u,v = q.popleft()
                for du,dv in dirs:
                    nu, nv = du+u, dv+v
                    if 0<=nu<n and 0<=nv<m and (nu,nv) not in visited:
                        if heights[nu][nv]>=heights[u][v]:
                            q.append((nu,nv))
                            visited.add((nu,nv))
                
            return visited
        pac = bfs(pacific)
        atl = bfs(atlantic)
        intersection = pac&atl
        return [[i,j] for i,j in intersection]
        


