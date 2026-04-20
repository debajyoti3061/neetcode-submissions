class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0

        def dfs(grid,i,j):
            if i < 0 or i >= len(grid) or j < 0 or j>= len(grid[i]) or grid[i][j] == 0: 
                return 0
            grid[i][j] = 0
            count = 1
            count += dfs(grid,i+1,j)
            count += dfs(grid, i-1,j)
            count += dfs(grid,i,j+1)
            count += dfs(grid,i,j-1)
            return count

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, dfs(grid,i,j))
        return maxArea