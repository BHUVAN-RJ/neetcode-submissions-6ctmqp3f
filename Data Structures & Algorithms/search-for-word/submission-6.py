class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = set()
        ROWS = len(board)
        COLS = len(board[0])

        def dfs(i, r, c):
            if len(word) == i:
                return True
            
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or word[i] != board[r][c] or (r,c) in path:
                return

            path.add((r,c))
            res = (dfs(i+1, r + 1, c) or
                    dfs(i+1, r - 1, c) or
                    dfs(i+1, r, c+1) or
                    dfs(i+1, r, c - 1) )
            path.remove((r,c))
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(0, r, c):
                    return True
        
        return False
            

        