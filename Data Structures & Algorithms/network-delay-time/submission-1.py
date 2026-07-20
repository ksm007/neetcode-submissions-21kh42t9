class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visit = set()
        dic = defaultdict(list)
        for s,d,w in times:
            dic[s].append((d,w))
        minH = []
        for d, w in dic[k]:
            minH.append([w,k,d])
        heapq.heapify(minH)
        t = 0
        visit.add(k)
        while minH:
            w, s, d = heapq.heappop(minH)
            if d in visit:
                continue
            t=w
            visit.add(d)
            if len(visit) == n:
                return t

            for des, wei in dic[d]:
                if des in visit:
                    continue
                heapq.heappush(minH,[wei+t,d,des])
        return -1
