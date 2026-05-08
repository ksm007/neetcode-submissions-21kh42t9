class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        adjList = {i:[] for i in range(n)}
        for s,d in edges:
            adjList[s].append(d)
            adjList[d].append(s)
        
        visit = set()
        def dfs(node, prev):
            if node in visit:
                return False
            visit.add(node)
            for n in adjList[node]:
                if n == prev:
                    continue
                if not dfs(n,node):
                    return False
            return True
        
        return dfs(0,-1) and len(visit) ==n

