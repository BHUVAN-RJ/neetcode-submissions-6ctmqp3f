class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[] for i in range(len(board))]
        cols = [[] for i in range(len(board[0]))]
        grids = [[[] for i in range(len(board) // 3)] for j in range(len(board) // 3)]
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == '.':
                    continue
                if board[i][j] in rows[i]:
                    print('rows')
                    return False
                if board[i][j] in cols[j]:
                    print('cols')
                    return False

                if board[i][j] in grids[i//3][j//3]:
                    print('sha')
                    print(grids, i,j)
                    return False
                rows[i].append(board[i][j])
                cols[j].append(board[i][j])
                grids[i//3][j//3].append(board[i][j])
        return True



        