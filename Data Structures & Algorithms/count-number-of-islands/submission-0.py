class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        island = 0
        visited = [[False for j in range(cols)] for i in range(rows)]

        def visitIsland(i, j):
            visited[i][j] = True
            if i - 1 >= 0 and not visited[i - 1][j] and grid[i - 1][j] == "1":
                visitIsland(i - 1, j)
            if i + 1 < rows and not visited[i + 1][j] and grid[i + 1][j] == "1":
                visitIsland(i + 1, j)
            if j - 1 >= 0 and not visited[i][j - 1] and grid[i][j - 1] == "1":
                visitIsland(i, j - 1)
            if j + 1 < cols and not visited[i][j + 1] and grid[i][j + 1] == "1":
                visitIsland(i, j + 1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "0" or visited[i][j]:
                    continue
                print(grid[i][j], i,j)
                island += 1
                visitIsland(i, j)
        return island
        