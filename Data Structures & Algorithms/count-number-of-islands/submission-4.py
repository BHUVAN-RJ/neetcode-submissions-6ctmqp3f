class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        ROWS, COLS = len(grid), len(grid[0])
        self.visited = [[False] * COLS for i in range(ROWS)]

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or self.visited[r][c] or grid[r][c] == '0':
                return
            self.visited[r][c] = True
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            return
            

        

        for r in range(ROWS):
            for c in range(COLS):
                if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == '0' or self.visited[r][c]:
                    continue
                
                count += 1
                dfs(r, c)
        return count

        