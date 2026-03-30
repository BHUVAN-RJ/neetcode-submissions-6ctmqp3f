class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False for j in range(len(grid[0]))] for i in range(len(grid))]
        def get_neighbours(i, j):
            if i > 0 and not visited[i-1][j] and grid[i-1][j] == "1":
                visited[i-1][j] = True
                get_neighbours(i-1,j)
            if i < len(grid) - 1 and not visited[i+1][j] and grid[i+1][j] == "1":
                visited[i+1][j] = True
                get_neighbours(i+1,j)
            if j > 0  and not visited[i][j-1] and grid[i][j-1] == "1":
                visited[i][j-1] = True
                get_neighbours(i,j-1)
            if j < len(grid[0]) - 1 and not visited[i][j+1] and grid[i][j+1] == "1":
                visited[i][j+1] = True
                get_neighbours(i,j+1)

        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j] and grid[i][j] == "1":
                    print(i,j)
                    islands += 1
                    visited[i][j] = True
                    get_neighbours(i,j)
        return islands