class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.visited = set()
        self.r=len(grid)
        self.c=len(grid[0])
        self.count=0

        def bfs(root):
            q = deque()
            q.append(root)
            dirs = [[0,1], [1,0],[-1,0],[0,-1]]
            while q:
                i,j = q.popleft()
                for dx, dy in dirs:
                    if 0<=i+dx<self.r and 0<=j+dy<self.c and grid[i+dx][j+dy]=="1" and (i+dx,j+dy) not in self.visited:
                        self.visited.add((i+dx,j+dy))
                        q.append((i+dx,j+dy))


        print(self.visited)
        for r in range(self.r):
            for c in range(self.c):
               
                if (r,c) not in self.visited and grid[r][c]=="1":
                    print(r,c)
                    self.count+=1
                    self.visited.add((r,c))
                    bfs((r,c))
        return self.count


