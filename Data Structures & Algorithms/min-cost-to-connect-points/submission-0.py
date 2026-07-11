class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        res = 0
        adj = {x:[] for x in range(N)}

        for i in range(N):
            x1,y1 = points[i]
            for j in range(i+1, N):
                x2,y2 = points[j]
                currCost = abs(x1-x2) + abs(y1-y2)
                adj[i].append([currCost, j])
                adj[j].append([currCost, i])
        
        minH = [[0,0]]
        visit = set()

        while len(visit) <N:

            cost,point = heapq.heappop(minH)
            if point in visit:
                continue
            res += cost
            visit.add(point)
            for neiCost,nei in adj[point]:
                if nei not in visit:
                    heapq.heappush(minH,[neiCost,nei])
        
        return res