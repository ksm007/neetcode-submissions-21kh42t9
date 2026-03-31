class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        row = len(grid)
        col = len(grid[0])
        goodFruits = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    goodFruits+=1
        

        time = 0
        while(q and goodFruits>0):
            iters = [[1,0],[-1,0],[0,1],[0,-1]]
            for _ in range(len(q)):
                ro,co = q.popleft() 
                for r,c in iters:
                    if 0<= ro+r <row and 0 <= co+c < col and grid[ro+r][co+c] == 1:
                        grid[ro+r][co+c] = 2
                        goodFruits-=1
                        q.append((ro+r,co+c))
            if q:
                time+=1

        return time if goodFruits==0 else -1

        