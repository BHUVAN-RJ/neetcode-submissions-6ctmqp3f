class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])
        rows = [[] for i in range(ROWS)]
        cols = [[] for i in range(ROWS)]
        grids = [[[] for j in range(COLS // 3)] for i in range(ROWS // 3)]

        for i in range(ROWS):
            for j in range(COLS):
                curNum = board[i][j]
                if curNum == '.':
                    continue
                if curNum in rows[i]:
                    print('row', i , j)
                    return False
                if curNum in cols[j]:
                    print('col', i, j)
                    return False
                if curNum in grids[i // 3][j // 3]:
                    print('grid')
                    return False
                rows[i].append(curNum)
                cols[j].append(curNum)
                grids[i // 3][j // 3].append(curNum)
        
        print(grids, rows, cols)
        return True
                
        