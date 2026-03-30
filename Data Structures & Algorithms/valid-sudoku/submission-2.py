class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])
        rows = [[] for i in range(ROWS)]
        cols = [[] for i in range(COLS)]
        grids = [[[] for j in range(ROWS // 3)] for i in range(COLS // 3)]
        print(rows, cols, grids)
    
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == '.':
                    continue
                if board[i][j] in rows[i]:
                    return False
                if board[i][j] in cols[j]:
                    return False
                if board[i][j] in grids[i // 3][j // 3]:
                    return False
                rows[i].append(board[i][j])
                cols[j].append(board[i][j])
                grids[i // 3][j // 3].append(board[i][j])
        
        return True