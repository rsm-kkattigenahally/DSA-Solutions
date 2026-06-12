class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        self.visited = set()
        count = 0
        adj = {x:[] for x in range(n)}
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def bfs(root, adj):
            q = deque([root])
            while q:
                node = q.popleft()
                for ngb in adj[node]:
                    if ngb not in self.visited:
                        self.visited.add(ngb)
                        q.append(ngb)
            
        for i in range(n):
            if i not in self.visited:
                self.visited.add(i)
                bfs(i, adj)
                count+=1
        return count