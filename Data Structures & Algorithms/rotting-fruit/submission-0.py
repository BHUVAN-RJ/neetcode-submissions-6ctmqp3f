'''
0 - empty
1- fresh 
2 - rotten


while i  - > break no state change -> break and check if all rooten
yes - >return i 
no -> -1
'''


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        freshFruits = 0


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    freshFruits += 1
                elif grid[r][c] == 2:
                    q.append([r, c])

        time = 0
        while q and freshFruits:# 
            time += 1 # 1
            for i in range(len(q)):# 1
                r,c = q.popleft()
                if r + 1 < ROWS and grid[r + 1][c] == 1:
                    q.append([r+1, c])
                    freshFruits -= 1
                    grid[r + 1][c] = 2
                if r - 1 >= 0 and grid[r - 1][c] == 1:
                    q.append([r-1, c])
                    freshFruits -= 1
                    grid[r - 1][c] = 2
                if c + 1 < COLS and grid[r][c + 1] == 1:
                    q.append([r, c + 1])
                    freshFruits -= 1
                    grid[r][c + 1] = 2
                if c - 1 >= 0 and grid[r][c - 1] == 1:
                    q.append([r, c - 1])
                    freshFruits -= 1
                    grid[r][c - 1] = 2
                

            
        if freshFruits:
            return -1
        
        return time
















        