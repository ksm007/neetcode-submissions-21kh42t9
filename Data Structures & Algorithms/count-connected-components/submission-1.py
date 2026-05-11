class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        for s,d in edges:
            adj[s].append(d)
            adj[d].append(s)
        res = 0
        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neigh in adj[node]:
                dfs(neigh)

        for i in range(n):
            if i not in visited:
                dfs(i)
                res+=1
        return res

            
