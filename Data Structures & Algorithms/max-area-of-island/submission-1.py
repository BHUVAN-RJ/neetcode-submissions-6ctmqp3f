class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        ROWS, COLS = len(grid), len(grid[0])
        visited = [[False for i in range(COLS)] for i in range(ROWS)]

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or visited[r][c] or grid[r][c] == 0:
                return 0
            visited[r][c] = True
            area = 1
            area += dfs(r-1, c)
            area += dfs(r+1, c)
            area += dfs(r, c - 1)
            area += dfs(r, c+1)

            return area
        
        for r in range(ROWS):
            for c in range(COLS):
                if r < 0 or c < 0 or r >= ROWS or c >= COLS or visited[r][c] or grid[r][c] == 0:
                    continue
                area = dfs(r, c)
                maxArea = max(area, maxArea)
        
        return maxArea


        
        