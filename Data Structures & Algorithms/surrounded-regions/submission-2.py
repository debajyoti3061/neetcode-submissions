class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS , COLS = len(board), len(board[0])

        def dfs(r,c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] != 'O':
                return
            board[r][c] = 'T'
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        for i in range(0,ROWS):
            for j in range(0,COLS):
                if board[i][j] == 'O' and (i in [0,ROWS-1] or j in [0,COLS-1]):
                    dfs(i,j)
        
        for i in range(0,ROWS):
            for j in range(0,COLS):
                if board[i][j] != 'T':
                    board[i][j] = 'X'
        for i in range(0,ROWS):
            for j in range(0,COLS):
                if board[i][j] == 'T':
                    board[i][j] = 'O'
        