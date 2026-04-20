class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[] for j in range(len(board[0]))]
        cols = [[] for j in range(len(board[0]))]
        grids = [[[] for i in range(len(board) // 3)] for j in range(len(board[0])//3)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                if board[i][j] in rows[i]:
                    return False
                else:
                    rows[i].append(board[i][j])
                
                if board[i][j] in cols[j]:
                    return False
                else:
                    cols[j].append(board[i][j])
                
                if board[i][j] in grids[int(i / 3)][int(j/3)]:
                    return False
                else:
                    grids[int(i / 3)][int(j/3)].append(board[i][j])
        return True


        