class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {s:[] for s,d in tickets }

        tickets.sort()
        for s,d in tickets:
            adj[s].append(d)
        

        res = ["JFK"]

        def dfs(node):
            if len(res) == len(tickets) + 1:
                return True
            if node not in adj:
                return False
            
            temp = list(adj[node])
            for i,val in enumerate(temp):
                adj[node].pop(i)
                res.append(val)
                if dfs(val): return True
                adj[node].insert(i,val)
                res.pop()
            
        dfs("JFK")
        return res