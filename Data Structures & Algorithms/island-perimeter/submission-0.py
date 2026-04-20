class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(i,j):
            if i >= len(grid) or j >= len(grid[0]) or i < 0 or j <0 or grid[i][j] == 0 :
                return 1
            if (i,j) in visited:
                return 0
            visited.add((i,j))
            perim = dfs(i,j+1)+ dfs(i,j-1) + dfs(i-1,j) + dfs(i+1,j)
            return perim

        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    return dfs(i,j)
        return 0

        