class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if grid == []:      #if not grid:
            return 0
        
        maxrow, maxcol = len(grid), len(grid[0])
        islands = 0
        
        def dfs(r, c):
            if grid[r][c] == '1':
                grid[r][c] = '0'
                if r >= 1: dfs(r-1, c)
                if r+1 < maxrow: dfs(r+1, c)
                if c >= 1: dfs(r, c-1)
                if c+1 < maxcol: dfs(r, c+1)
        
        for i in range(maxrow):
            for j in range(maxcol):
                if grid[i][j] == '1':
                    dfs(i, j)
                    islands += 1
        
        return islands