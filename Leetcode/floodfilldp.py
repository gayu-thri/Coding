class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        maxrow, maxcol = len(image), len(image[0])
        startColor = image[sr][sc]
        
        if startColor == newColor:
            return image
        def dfs(r, c):
            if image[r][c] == startColor:
                image[r][c] = newColor
                
                if r >= 1: dfs(r-1, c)
                if r+1 < maxrow: dfs(r+1, c)
                if c >= 1: dfs(r, c-1)
                if c+1 < maxcol: dfs(r, c+1)
        
        dfs(sr, sc)
        return image