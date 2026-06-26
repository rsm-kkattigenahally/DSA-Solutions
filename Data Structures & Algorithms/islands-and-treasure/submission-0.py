class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited = set()
        n = len(grid)
        m = len(grid[0])

        
        q = deque([])
        for i in range(n):
            for j in range(m):
                if grid[i][j]==0:
                    q.append((i,j))
        while q:
            u,v = q.popleft()
            dirs = [[-1,0],[1,0],[0,-1],[0,1]]
            for du,dv in dirs:
                nu, nv = du+u, dv+v
                if 0<=nu<n and 0<=nv<m and (nu,nv) not in visited:
                    if grid[nu][nv]==2147483647:
                        grid[nu][nv] = 1 + grid[u][v]
                        q.append((nu,nv))
                        visited.add((nu,nv))
                    elif grid[nu][nv]==-1: continue
            
       

