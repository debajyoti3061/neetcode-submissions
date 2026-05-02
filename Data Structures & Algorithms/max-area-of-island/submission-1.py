"""
REVISION NOTES - Max Area Of Island:
• Use DFS to explore each island and count its area
• Mark visited cells as 0 to avoid revisiting
• For each land cell (1), start DFS and count connected land cells
• DFS returns area of current island by summing 1 + areas of 4 directions
• Track maximum area found across all islands
• Time: O(m*n), Space: O(m*n) for recursion stack
"""

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