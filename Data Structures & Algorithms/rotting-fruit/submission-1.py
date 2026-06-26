class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        q = deque([])
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    q.append((i,j))
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]
        minutes = 0
        while q:
            minutes+=1
            for _ in range(len(q)):
                u,v = q.popleft()
                for du,dv in dirs:
                    nu, nv = u+du, v+dv
                    if 0<=nu<n and 0<=nv<m and grid[nu][nv]==1:
                        grid[nu][nv]=2
                        q.append((nu,nv))
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1: return -1
        if minutes == 0: return 0
        return minutes-1
        