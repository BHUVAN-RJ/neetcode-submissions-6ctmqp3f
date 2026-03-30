class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        num_islands = 0
        print(visited)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j]:
                    print(i,j)
                    if int(grid[i][j]) == 1:
                        print(i,j, visited)
                        visited[i][j] = True
                        self.check_neighbours(i,j, visited, grid)
                        num_islands += 1
                    
        return num_islands

    def check_neighbours(self, i, j, visited, grid):
        if i > 0 and not visited[i-1][j] and int(grid[i-1][j]) == 1:
            visited[i-1][j] = True
            self.check_neighbours(i-1, j, visited, grid)
        if i < len(grid) - 1 and not visited[i+1][j] and int(grid[i+1][j]) == 1:
            visited[i+1][j] = True
            self.check_neighbours(i+1, j, visited, grid)
        if j > 0 and  not visited[i][j-1] and int(grid[i][j - 1]) == 1:
            visited[i][j - 1] = True
            self.check_neighbours(i, j - 1, visited, grid)
        if j < len(grid[0]) - 1 and not visited[i][j+1]  and int(grid[i][j+1]) == 1:
            visited[i][j + 1] = True
            self.check_neighbours(i, j+1, visited, grid)
