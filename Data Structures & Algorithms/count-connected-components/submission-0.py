class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        for s,d in edges:
            adj[s].append(d)
            adj[d].append(s)
        res = 0
        visited = [False] * n
        def dfs(node):

            for no in adj[node]:
                if not visited[no]:
                    visited[no] = True
                    dfs(no)
        
        for node in range(n):
            if not visited[node]:
                visited[node] = True
                dfs(node)
                res+=1
        return res

            
