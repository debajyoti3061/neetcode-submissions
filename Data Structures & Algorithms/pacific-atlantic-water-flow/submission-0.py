class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(row, col,visited, prevHeight):
            if (row,col) in visited or row < 0 or col < 0 or row == ROWS or col == COLS or heights[row][col] < prevHeight:
                return
            visited.add((row,col))
        
            dfs(row-1, col,visited, heights[row][col])
            dfs(row+1, col,visited, heights[row][col])
            dfs(row, col-1,visited, heights[row][col])
            dfs(row, col+1,visited, heights[row][col])


        for c in range(COLS):
            dfs(0,c,pac,heights[0][c])
            dfs(ROWS-1,c,atl,heights[ROWS-1][c])
        
        for r in range(ROWS):
            dfs(r,0,pac,heights[r][0])
            dfs(r,COLS-1,atl,heights[r][COLS-1])
        res = []
        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) in pac and (i,j) in atl:
                    res.append([i,j])
        return res

        