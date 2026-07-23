class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visit = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        def dfs(r,c):
            if (r < 0 or r > ROWS - 1 or c < 0 or 
            c > COLS - 1 or  grid[r][c] == 0):
                return 1
            if (r,c) in visit:
                return 0
            visit.add((r,c))
            perim = dfs(r-1,c)+ dfs(r,c-1) +dfs(r+1,c) + dfs(r,c+ 1)
            return perim
        

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visit:
                    return dfs(r,c)

