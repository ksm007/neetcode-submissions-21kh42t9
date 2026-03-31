class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows,cols = len(grid), len(grid[0])
        visited  = set()
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))
        
        dist = 0

        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist
                iters = [(-1,0),(1,0),(0,1),(0,-1)]
                for dr,dc in iters:
                    row,col = r+dr,c+dc
                    if 0<= row <rows and 0<= col < cols and (row,col) not in visited and grid[row][col] !=-1:
                        visited.add((row,col))
                        q.append((row,col))
            dist+=1