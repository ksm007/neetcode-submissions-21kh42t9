class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adj = {i:[] for i in range(1,n+1)}

        for s,d in trust:
            adj[s].append(d)
        probableJudge = -1
        for k, v in adj.items():
            if len(v) == 0:
                probableJudge = k
        if probableJudge == -1:
            return -1
        for k, v in adj.items():
            if k !=probableJudge and probableJudge not in v:
                return -1
        return probableJudge


